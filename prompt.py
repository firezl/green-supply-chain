import pandas as pd
import numpy as np
from bot import Conversation
from vars import meaning_dict
import os

# Replace <api_key> with your actual API key, ensuring it is a string.

api_key = os.environ.get("API_KEY")

Chinese_prompt = "你现在是一个ESG分析师，你需要对一家公司在ESG中环境方面的表现进行评估。我将会给你一些关于这家公司在绿色供应链和碳中和方面的信息。\
    你需要根据这些信息，给出[A+,A,A-,B+,B,B-,C+,C,C-]中的一个评级。你的回答必须按照以下格式：公司名：评级"
English_prompt = "You are an ESG analyst, and you need to evaluate the company's performance in ESG environment. \
    I will give you some information about the company's performance in green supply chain and carbon neutrality.\
    You need to give a rating of [A+,A,A-,B+,B,B-,C+,C,C-] based on this information. Your answer must be in the following format: Company name: rating"


def Chinese_question_template(data):
    question = "公司名称：{}，公司区域：{}，股票代码：{}，公司行业：{}，绿色供应链指数：{}，绿色供应链指数全球排名：{}，绿色供应链指数行业排名：{}，绿色供应链行动指数：{}，绿色供应链行动指数全球排名：{}，绿色供应链行动指数行业排名：{}，碳排放量减少：{}，碳排放量：{}，客户集中度：{}，供应商集中度：{}，客户集中度赫芬达尔指数：{}，供应商集中度赫芬达尔指数：{}，供应链集中度：{}。"
    question = question.format(
        data["Company_name"],
        data["Company_area"],
        data["Company_code"],
        data["Company_industry"],
        data["CITI"],
        data["CITI_all_rank"],
        data["CITI_trade_rank"],
        data["CATI"],
        data["CATI_all_rank"],
        data["CATI_trade_rank"],
        data["CEmissReduce"],
        data["CEmission"],
        data["SC_CC"],
        data["SC_PC"],
        data["SC_CCHHI"],
        data["SC_PCHHI"],
        data["SC_SCC"],
    )
    return question


def English_question_template(data):
    Compant_name = data["Company_name"]
    question = "Company name: {}, Company area: {}, Company code: {}, Company industry: {}, CITI: {}, CITI all rank: {}, CITI trade rank: {}, CATI: {}, CATI all rank: {}, CATI trade rank: {}, Carbon emission reduce: {}, Carbon emission: {}, Customer concentration: {}, Supplier concentration: {}, Customer concentration Herfindahl index: {}, Supplier concentration Herfindahl index: {}, Supply chain concentration: {}."
    question = question.format(
        data["Company_name"],
        data["Company_area"],
        data["Company_code"],
        data["Company_industry"],
        data["CITI"],
        data["CITI_all_rank"],
        data["CITI_trade_rank"],
        data["CATI"],
        data["CATI_all_rank"],
        data["CATI_trade_rank"],
        data["CEmissReduce"],
        data["CEmission"],
        data["SC_CC"],
        data["SC_PC"],
        data["SC_CCHHI"],
        data["SC_PCHHI"],
        data["SC_SCC"],
    )
    return question


# 读取数据
data = pd.read_excel("data/data_cn_lc.xlsx")

# 提问
conversation = Conversation(api_key, "Claude-instant", English_prompt)
for i in range(0, 10):
    result = conversation.chat(English_question_template(data.iloc[i, :]))
    print(result)
