import pandas as pd
import numpy as np
import re
from bot import Conversation
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
from prompt_advise import (
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
LLM = "GPT-4o-Mini"

save_path = "./result"

try:
    os.makedirs(save_path)
except:
    pass

console = Console()
wrong_index = np.load("./wrong_index.npy")
for i in range(len(data)):
    if i not in wrong_index:
        continue
    conversation = Conversation(api_key, LLM, Chinese_prompt)
    result = ""
    while result == "":
        try:
            result = conversation.chat(Chinese_question_template(data.iloc[i, :]))
        except:
            continue

    with open(f"{save_path}/{i}.md", "w") as f:
        f.write(Chinese_question_template(data.iloc[i, :]))
        f.write("\n")
        f.write(result)

    markdown = Markdown(result)
    console.print(markdown)
    console.print("")
