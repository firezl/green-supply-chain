import pandas as pd
import numpy as np
from bot import Conversation
from vars import meaning_dict
import os

# Replace <api_key> with your actual API key, ensuring it is a string.

api_key = os.environ.get("API_KEY")

Chinese_prompt = "你现在是一个绿色供应链管理者,你需要根据公司的绿色供应链表现指出该公司哪些方面需要进行改进。你的建议将包含以下几个方面:\
    供应链（范围3）政策宣示; \
    供应链（范围3）测算披露; \
    供应链（范围3）目标设定; \
    供应链（范围3）目标绩效; \
    供应链（范围3）供应商企业自主开展碳管理; \
    范围1+2 政策宣示;\
    范围1+2 测算披露; \
    范围1+2 目标设定; \
    范围1+2 目标绩效; \
    范围1+2 自身减排行动; \
    你的回答需要按照下面的格式:[方面]: [是否已经实施], 如果没有实施, [建议措施]。"
English_prompt = "You are a green supply chain manager, and you need to point out which aspects of the company need to be improved based on the company's performance in green supply chain. Your advice will include the following aspects: \
    Supply chain (scope 3) policy declaration; \
    Supply chain (scope 3) calculation and disclosure; \
    Supply chain (scope 3) target setting; \
    Supply chain (scope 3) target setting; \
    Supply chain (scope 3) target performance; \
    Supply chain (scope 3) supplier enterprise independently carry out carbon management; \
    Scope 1+2 policy declaration; \
    Scope 1+2 calculation and disclosure; \
    Scope 1+2 target setting; \
    Scope 1+2 target performance; \
    Scope 1+2 self-reduction action; \
    Your answer must be in the following format: [Aspect]: [Whether it has been implemented], if not, [suggested measures]."


def Chinese_question_template(data):
    question = "公司名称:{},公司区域:{},股票代码:{},公司行业:{};\
        绿色供应链指数:{},绿色供应链指数全球排名:{},绿色供应链指数行业排名:{},绿色供应链行动指数:{},绿色供应链行动指数全球排名:{},绿色供应链行动指数行业排名:{};\
        碳排放量减少:{},碳排放量:{};\
        客户集中度:{},供应商集中度:{},客户集中度赫芬达尔指数:{},供应商集中度赫芬达尔指数:{},供应链集中度:{};\
        供应链（范围3）政策宣示 将供应商温室气体核算与报送纳入供应商行为准则:{};\
        供应链（范围3）政策宣示 引导低碳、可持续消费,开展价值链减排: {};\
        供应链（范围3）测算披露 测算并披露范围3排放量: {};\
        供应链（范围3）测算披露 定期收集供应商实际排放数据: {};\
        供应链（范围3）目标设定 设定并披露正在执行的范围3减排目标: {}\
        供应链（范围3）目标设定 设定并披露范围3碳中和目标: {}\
        供应链（范围3）目标设定 设定并披露的目标涵盖：推动供应商设定减排目标: {}\
        供应链（范围3）目标绩效 披露范围3减排目标的完成进展: {}\
        供应链（范围3）目标绩效 披露范围3碳中和目标的完成进展: {}\
        供应链（范围3）目标绩效 通过蔚蓝生态链或等效自动化系统跟踪供应商目标设定的进展（至少包括在华供应商）: {}\
        供应链（范围3）供应商企业自主开展碳管理 直接供应商自主核算并公开披露年度排放数据: {}\
        供应链（范围3）供应商企业自主开展碳管理 直接供应商自主设定并公开披露目标与进展: {}\
        供应链（范围3）供应商企业自主开展碳管理 间接供应商自主核算并公开披露年度排放数据: {}\
        供应链（范围3）供应商企业自主开展碳管理 间接供应商自主设定并公开披露目标与进展: {}\
        供应链（范围3）供应商企业自主开展碳管理 企业通过蔚蓝生态链或等效自动化系统赋能上游供应商开展供应链碳管理: {}\
        范围1+2 政策宣示 制定企业碳中和配套管理制度: {}\
        范围1+2 测算披露 测算并披露范围1&2排放量: {}\
        范围1+2 测算披露 测算并披露碳强度: {}\
        范围1+2 目标设定 设定并披露正在执行的范围1&2减排目标: {}\
        范围1+2 目标设定 设定并披露范围1&2碳中和目标: {}\
        范围1+2 目标绩效 披露范围1&2减排目标的完成进展: {}\
        范围1+2 目标绩效 披露范围1&2碳中和目标的完成进展: {}\
        范围1+2 自身减排行动 开展非化石能源利用项目，并披露项目减排量: {}\
        范围1+2 自身减排行动 开展能效提升技术应用项目，并披露项目减排量: {}\
        范围1+2 自身减排行动 开展能源监测和管理项目: {}\
        范围1+2 自身减排行动 通过碳抵消机制减排，并披露项目减排量: {}\
        范围1+2 自身减排行动 推动其自有工厂、下属子公司、门店等披露碳排放数据，且/或设定减排目标: {}"
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
        data["Band_1"],
        data["Band_2"],
        data["Band_3"],
        data["Band_4"],
        data["Band_5"],
        data["Band_6"],
        data["Band_7"],
        data["Band_8"],
        data["Band_9"],
        data["Band_10"],
        data["Band_11"],
        data["Band_12"],
        data["Band_13"],
        data["Band_14"],
        data["Band_15"],
        data["Band_16"],
        data["Band_17"],
        data["Band_18"],
        data["Band_19"],
        data["Band_20"],
        data["Band_21"],
        data["Band_22"],
        data["Band_23"],
        data["Band_24"],
        data["Band_25"],
        data["Band_26"],
        data["Band_27"],
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
