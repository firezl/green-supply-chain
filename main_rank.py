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
import os

api_key = os.environ.get("API_KEY")

# 读取数据
data = pd.read_excel("data/data_cn_lc.xlsx")

# 提问
LLM = "GPT-4"
iteration = "0"
data["rank_" + LLM + iteration] = ["-"] * len(data)
# data.to_excel("data/data_cn_lc.xlsx", index=False)

conversation = Conversation(api_key, LLM, Chinese_prompt)

console = Console()

success = 0

while success == 0:
    success = 1
    for i in track(range(0, len(data))):
        success = 0
        # data.to_excel("data/data_cn_lc.xlsx", index=False)
        conversation = Conversation(api_key, LLM, Chinese_prompt)
        result = ""
        while result == "":
            try:
                result = conversation.chat(Chinese_question_template(data.iloc[i, :]))
            except Exception:
                continue
        markdown = Markdown(result)
        console.print(markdown)


# 保存结果

# data.to_excel("data/data_cn_lc.xlsx", index=False)
console.print("Done!", style="bold blue")
