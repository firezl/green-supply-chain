import pandas as pd
import numpy as np
import re
from bot import Conversation
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
from prompt import (
    Chinese_prompt,
    English_prompt,
    Chinese_question_template,
    English_question_template,
)
import os

api_key = os.environ.get("API_KEY")

# 读取数据
data = pd.read_excel("data/data_cn_lc.xlsx")

# 提问
LLM = "ChatGPT"

data["rank_" + LLM] = ["-"] * len(data)
data.to_excel("data/data_cn_lc.xlsx", index=False)

conversation = Conversation(api_key, LLM, Chinese_prompt)

console = Console()

success = 0

while success == 0:
    success = 1
    for i in track(range(0, len(data))):
        if data.loc[i, "rank_" + LLM] != "-":
            continue
        success = 0
        if i % 20 == 0:
            data.to_excel("data/data_cn_lc.xlsx", index=False)
            conversation = Conversation(api_key, LLM, Chinese_prompt)
        try:
            result = conversation.chat(Chinese_question_template(data.iloc[i, :]))
        except Exception:
            console.print_exception(show_locals=True)
            continue
        index = max(result.find(":"), result.find("："))
        rank = result[index + 1 : index + 3]
        rank = rank.replace("\n", "")
        if rank == "":
            rank = "-"
        if rank not in [
            "A+",
            "A",
            "A-",
            "B+",
            "B",
            "B-",
            "C+",
            "C",
            "C-",
            "D+",
            "D",
            "D-",
            "-",
        ]:
            rank = "-"
        data.loc[i, "rank_" + LLM] = rank
        markdown = Markdown(result)
        console.print(markdown)
        console.print(rank, style="bold green")

# 保存结果

data.to_excel("data/data_cn_lc.xlsx", index=False)
console.print("Done!", style="bold blue")
