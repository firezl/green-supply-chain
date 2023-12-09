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
LLM = "ChatGPT"

console = Console()

for i in range(len(data)):
    conversation = Conversation(api_key, LLM, Chinese_prompt)
    try:
        result = conversation.chat(Chinese_question_template(data.iloc[i, :]))
    except:
        console.print("Error!")
        continue
    markdown = Markdown(result)
    console.print(markdown)
    console.print("")
