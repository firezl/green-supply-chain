from email import message
import os
from openai import OpenAI
import pandas as pd
import numpy as np
import re
from bot import Conversation
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
from prompt_rank import (
    Chinese_prompt,
    English_prompt,
    Chinese_question_template,
    English_question_template,
)

from SALib.sample import saltelli
from SALib.analyze import sobol

api_key = "fk198525-0QxRTQUeNOsFCMlwXml0nhUNzka0Sa4I"

# 读取数据
data = pd.read_excel("data/data_cn_lc.xlsx")


# 提问
LLM = "gpt-4o-mini"
iteration = "1"
data["rank_" + LLM + iteration] = ["-"] * len(data)
# data.to_excel("data/data_cn_lc.xlsx", index=False)

clinet = OpenAI(api_key=api_key, base_url="https://oa.api2d.net")

console = Console()


def get_result(data):
    result = ""
    while result == "":
        try:
            message = [
                {
                    "role": "system",
                    "content": Chinese_prompt,
                },
                {
                    "role": "user",
                    "content": Chinese_question_template(data),
                },
            ]
            chat_completion = clinet.chat.completions.create(
                messages=message, model=LLM
            )
            result = chat_completion.choices[0].message.content
        except Exception as e:
            console.print(e, style="bold red")
            continue
    # 从result中提取答案(匹配ABCDEFG和A+-B+-C+-D+-E+-F+-G+-)
    rank = re.findall(r"[A-G][+-]", result)
    # 转化为一个字母
    if len(rank) == 0:
        rank = re.findall(r"[A-G]", result)
    if len(rank) == 0:
        return "-"
    return rank[0][0]


# 测试
# print(data.iloc[0, :])
# rank = get_result(data.iloc[0, :])
# print(rank)

problem = {
    "num_vars": 13,
    "names": [
        "CITI",
        "CITI_all_rank",
        "CITI_trade_rank",
        "CATI",
        "CATI_all_rank",
        "CATI_trade_rank",
        "CEmissReduce",
        "CEmission",
        "SC_CC",
        "SC_PC",
        "SC_CCHHI",
        "SC_PCHHI",
        "SC_SCC",
    ],
    "bounds": [
        [0, 100],
        [1, 741],
        [1, 126],
        [0, 100],
        [1, 1510],
        [1, 157],
        [0, 600000],
        [0, 600000],
        [0, 100],
        [0, 100],
        [0, 1],
        [0, 1],
        [0, 100],
    ],
}

Map = {
    "A+": 1,
    "A": 2,
    "A-": 3,
    "B+": 4,
    "B": 5,
    "B-": 6,
    "C+": 7,
    "C": 8,
    "C-": 9,
    "D+": 10,
    "D": 11,
    "D-": 12,
    "E+": 13,
    "E": 14,
    "E-": 15,
    "F+": 16,
    "F": 17,
    "F-": 18,
    "G+": 19,
    "G": 20,
    "G-": 21,
    "-": 22,
}

# 保存结果
param_values = saltelli.sample(problem, 2**5)
Y = np.zeros([param_values.shape[0]])
print(Y.shape)
for i, X in enumerate(track(param_values)):
    input_data = data.iloc[0, :]
    for j in range(len(X)):
        input_data[problem["names"][j]] = X[j]
    Y[i] = Map[get_result(input_data)]
    print(i)

Si = sobol.analyze(problem, Y, print_to_console=False)
print(Si)

Si.plot()

# data.to_excel("data/data_cn_lc.xlsx", index=False)
# console.print("Done!", style="bold blue")
