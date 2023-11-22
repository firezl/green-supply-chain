import requests
import bs4
import pandas as pd
import numpy as np
import os
from tqdm import tqdm
from typing import Any, List, Dict, Tuple, Optional, Union
from vars import meaning_dict, head, base_url1, base_url2


def parse_data(
    soup1: bs4.BeautifulSoup, soup2: bs4.BeautifulSoup
) -> List[Union[str, int, float]]:
    CITI = (
        soup1.find_all("ul", {"class": "citi-cati citi-number"})[0]
        .find_all("li")[0]
        .find("p")
        .text
    )

    CITI_all_rank = (
        soup1.find_all("ul", {"class": "citi-cati citi-number"})[0]
        .find_all("li")[1]
        .find("p")
        .text
    )

    CITI_trade_rank = (
        soup1.find_all("ul", {"class": "citi-cati citi-number"})[0]
        .find_all("li")[2]
        .find("p")
        .text
    )

    CATI = (
        soup1.find_all("ul", {"class": "citi-cati cati-number"})[0]
        .find_all("li")[0]
        .find("p")
        .text
    )

    CATI_all_rank = (
        soup1.find_all("ul", {"class": "citi-cati cati-number"})[0]
        .find_all("li")[1]
        .find("p")
        .text
    )

    CATI_trade_rank = (
        soup1.find_all("ul", {"class": "citi-cati cati-number"})[0]
        .find_all("li")[2]
        .find("p")
        .text
    )

    # 1. 沟通与透明（总分14）
    CITI_1 = soup1.find_all("div", {"class": "lists"})[0].find_all("strong")[0].text

    # 1.1 公众问责与沟通
    CITI_1_1 = soup1.find_all("div", {"class": "lists"})[0].find_all("strong")[1].text

    # 1.2 推动透明供应链
    CITI_1_2 = soup1.find_all("div", {"class": "lists"})[0].find_all("strong")[2].text

    # 2. 合规性与整改行动（总分18）
    CITI_2 = soup1.find_all("div", {"class": "lists"})[1].find_all("strong")[0].text

    # 2.1 检索供应商环境合规表项
    CITI_2_1 = soup1.find_all("div", {"class": "lists"})[1].find_all("strong")[1].text

    # 2.2 推动供应商整改及披露
    CITI_2_2 = soup1.find_all("div", {"class": "lists"})[1].find_all("strong")[2].text

    # 3. 延伸绿色供应链（总分30）
    CITI_3 = soup1.find_all("div", {"class": "lists"})[2].find_all("strong")[0].text

    # 3.1 化学品负责任管控
    CITI_3_1 = soup1.find_all("div", {"class": "lists"})[2].find_all("strong")[1].text

    # 3.2.1 污水负责任管控
    CITI_3_2_1 = soup1.find_all("div", {"class": "lists"})[2].find_all("strong")[2].text

    # 3.2.2 固体废物负责任管控
    CITI_3_2_2 = soup1.find_all("div", {"class": "lists"})[2].find_all("strong")[3].text

    # 3.3 物流负责任管控
    CITI_3_3 = soup1.find_all("div", {"class": "lists"})[2].find_all("strong")[4].text

    # 3.4 供应商自主管控环境风险
    CITI_3_4 = soup1.find_all("div", {"class": "lists"})[2].find_all("strong")[5].text

    # 4. 节能减排（总分32）
    CITI_4 = soup1.find_all("div", {"class": "lists"})[3].find_all("strong")[0].text

    # 4.1 推动供应商节能减排，披露能源与碳数据
    CITI_4_1 = soup1.find_all("div", {"class": "lists"})[3].find_all("strong")[1].text

    # 4.2 推动供应商提高资源利用效率、减少污染物排放，披露污染物排放转移数据
    CITI_4_2 = soup1.find_all("div", {"class": "lists"})[3].find_all("strong")[2].text

    # 5. 推动公众绿色选择（总分6）
    CITI_5 = soup1.find_all("div", {"class": "lists"})[4].find_all("strong")[0].text

    # 5.1 引导公众关注在华供应链环境表现
    CITI_5_1 = soup1.find_all("div", {"class": "lists"})[4].find_all("strong")[1].text

    # 1.1 治理机制-制度建设（总分5）
    CATI_1_1 = soup1.find_all("div", {"class": "lists"})[5].find_all("strong")[0].text

    # 1.1.1 已做出气候行动的承诺，发布气候宣言
    CATI_1_1_1 = soup1.find_all("div", {"class": "lists"})[5].find_all("strong")[1].text

    # 1.1.2 制定企业碳中和配套管理制度
    CATI_1_1_2 = soup1.find_all("div", {"class": "lists"})[5].find_all("strong")[2].text

    # 1.1.3 将供应商温室气体核算与报送纳入供应商行为准则等书面文件
    CATI_1_1_3 = soup1.find_all("div", {"class": "lists"})[5].find_all("strong")[3].text

    # 1.2 治理机制-机制建设（总分5）
    CATI_1_2 = soup1.find_all("div", {"class": "lists"})[6].find_all("strong")[0].text

    # 1.2.1 将气候变化纳入商业决策并具有针对气候相关的风险管理程序
    CATI_1_2_1 = soup1.find_all("div", {"class": "lists"})[6].find_all("strong")[1].text

    # 1.2.2 将气候相关议题纳入董事会（最高决策层）监督职责
    CATI_1_2_2 = soup1.find_all("div", {"class": "lists"})[6].find_all("strong")[2].text

    # 1.2.3 通过赋能、开展创新项目、财务激励等机制引导供应商减排
    CATI_1_2_3 = soup1.find_all("div", {"class": "lists"})[6].find_all("strong")[3].text

    # 2.1 测算披露-范围1&2（总分9）
    CATI_2_1 = soup1.find_all("div", {"class": "lists"})[7].find_all("strong")[0].text

    # 2.1.1 测算并披露范围1&2排放量
    CATI_2_1_1 = soup1.find_all("div", {"class": "lists"})[7].find_all("strong")[1].text

    # 2.1.2 测算并披露综合能耗和能源使用情况
    CATI_2_1_2 = soup1.find_all("div", {"class": "lists"})[7].find_all("strong")[2].text

    # 2.1.3 测算并披露碳强度或测算并披露能源强度
    CATI_2_1_3 = soup1.find_all("div", {"class": "lists"})[7].find_all("strong")[3].text

    # 2.1.4 披露碳排放交易情况
    CATI_2_1_4 = soup1.find_all("div", {"class": "lists"})[7].find_all("strong")[4].text

    # 2.2 测算披露-范围3 （总分：6.00）
    CATI_2_2 = soup1.find_all("div", {"class": "lists"})[8].find_all("strong")[0].text

    # 2.2.1 测算并披露范围3排放量
    CATI_2_2_1 = soup1.find_all("div", {"class": "lists"})[8].find_all("strong")[1].text

    # 2.2.2 定期收集供应商实际排放数据
    CATI_2_2_2 = soup1.find_all("div", {"class": "lists"})[8].find_all("strong")[2].text

    # 2.3 测算披露-产品碳足迹 （总分：4.00）
    CATI_2_3 = soup1.find_all("div", {"class": "lists"})[9].find_all("strong")[0].text

    # 2.3.1 测算并披露产品碳足迹数据
    CATI_2_3_1 = soup1.find_all("div", {"class": "lists"})[9].find_all("strong")[1].text

    # 3.1 碳目标设定-范围1&2目标 （总分：7.00）
    CATI_3_1 = soup1.find_all("div", {"class": "lists"})[10].find_all("strong")[0].text

    # 3.1.1 设定并披露正在执行的范围1&2减排目标
    CATI_3_1_1 = (
        soup1.find_all("div", {"class": "lists"})[10].find_all("strong")[1].text
    )

    # 3.1.2 设定并披露范围1&2碳中和目标
    CATI_3_1_2 = (
        soup1.find_all("div", {"class": "lists"})[10].find_all("strong")[2].text
    )

    # 3.1.3 设定并披露可再生能源目标
    CATI_3_1_3 = (
        soup1.find_all("div", {"class": "lists"})[10].find_all("strong")[3].text
    )

    # 3.1.4 范围1&2气候目标经专业机构认证或批准
    CATI_3_1_4 = (
        soup1.find_all("div", {"class": "lists"})[10].find_all("strong")[4].text
    )

    # 3.2 碳目标设定-范围3目标 （总分：7.00）
    CATI_3_2 = soup1.find_all("div", {"class": "lists"})[11].find_all("strong")[0].text

    # 3.2.1 设定并披露正在执行的范围3减排目标
    CATI_3_2_1 = (
        soup1.find_all("div", {"class": "lists"})[11].find_all("strong")[1].text
    )

    # 3.2.2 设定并披露范围3碳中和目标
    CATI_3_2_2 = (
        soup1.find_all("div", {"class": "lists"})[11].find_all("strong")[2].text
    )

    # 3.2.3 设定并披露的目标涵盖：推动供应商设定减排目标
    CATI_3_2_3 = (
        soup1.find_all("div", {"class": "lists"})[11].find_all("strong")[3].text
    )

    # 3.2.4 范围3气候目标经专业机构认证或批准
    CATI_3_2_4 = (
        soup1.find_all("div", {"class": "lists"})[11].find_all("strong")[4].text
    )

    # 4.1 碳目标绩效-范围1&2目标绩效 （总分：7.00）
    CATI_4_1 = soup1.find_all("div", {"class": "lists"})[12].find_all("strong")[0].text

    # 4.1.1 披露范围1&2减排目标的完成进展
    CATI_4_1_1 = (
        soup1.find_all("div", {"class": "lists"})[12].find_all("strong")[1].text
    )

    # 4.1.2 披露范围1&2碳中和目标的完成进展
    CATI_4_1_2 = (
        soup1.find_all("div", {"class": "lists"})[12].find_all("strong")[2].text
    )

    # 4.1.3 披露可再生能源目标的完成进展
    CATI_4_1_3 = (
        soup1.find_all("div", {"class": "lists"})[12].find_all("strong")[3].text
    )

    # 4.2 碳目标绩效-范围3目标绩效 （总分：7.00）
    CATI_4_2 = soup1.find_all("div", {"class": "lists"})[13].find_all("strong")[0].text

    # 4.2.1 披露范围3减排目标的完成进展
    CATI_4_2_1 = (
        soup1.find_all("div", {"class": "lists"})[13].find_all("strong")[1].text
    )

    # 4.2.2 披露范围3碳中和目标的完成进展
    CATI_4_2_2 = (
        soup1.find_all("div", {"class": "lists"})[13].find_all("strong")[2].text
    )

    # 4.2.3 跟踪并披露供应商目标设定的进展
    CATI_4_2_3 = (
        soup1.find_all("div", {"class": "lists"})[13].find_all("strong")[3].text
    )

    # 5.1 减排行动-企业自身运营减排 （总分：12.00）
    CATI_5_1 = soup1.find_all("div", {"class": "lists"})[14].find_all("strong")[0].text

    # 5.1.1 开展非化石能源利用或绿电采购项目，并披露项目减排量
    CATI_5_1_1 = (
        soup1.find_all("div", {"class": "lists"})[14].find_all("strong")[1].text
    )

    # 5.1.2 开展能源监测和管理项目
    CATI_5_1_2 = (
        soup1.find_all("div", {"class": "lists"})[14].find_all("strong")[2].text
    )

    # 5.1.3 开展能效提升技术应用项目，并披露项目减排量
    CATI_5_1_3 = (
        soup1.find_all("div", {"class": "lists"})[14].find_all("strong")[3].text
    )

    # 5.1.4 开展其他类型减排项目，并披露项目减排量
    CATI_5_1_4 = (
        soup1.find_all("div", {"class": "lists"})[14].find_all("strong")[4].text
    )

    # 5.1.5 通过碳市场抵消机制减排，并披露减排量
    CATI_5_1_5 = (
        soup1.find_all("div", {"class": "lists"})[14].find_all("strong")[5].text
    )

    # 5.2 减排行动-企业价值链减排 （总分：7.00）
    CATI_5_2 = soup1.find_all("div", {"class": "lists"})[15].find_all("strong")[0].text

    # 5.2.1 推动供应商开展企业碳管理或能源管理项目
    CATI_5_2_1 = (
        soup1.find_all("div", {"class": "lists"})[15].find_all("strong")[1].text
    )

    # 5.2.2 与产品生产相关供应商合作开展减排项目，并披露项目减排量
    CATI_5_2_2 = (
        soup1.find_all("div", {"class": "lists"})[15].find_all("strong")[2].text
    )

    # 5.2.3 与物流供应商合作开展减排项目，并披露项目减排量
    CATI_5_2_3 = (
        soup1.find_all("div", {"class": "lists"})[15].find_all("strong")[3].text
    )

    # 5.2.4 每年发布供应商减排最佳案例
    CATI_5_2_4 = (
        soup1.find_all("div", {"class": "lists"})[15].find_all("strong")[4].text
    )

    # 5.2.5 针对价值链上的其他排放源展开减排行动，并披露项目减排量
    CATI_5_2_5 = (
        soup1.find_all("div", {"class": "lists"})[15].find_all("strong")[5].text
    )

    # 5.3 减排行动-关联企业自主开展碳管理 （总分：8.00）
    CATI_5_3 = soup1.find_all("div", {"class": "lists"})[16].find_all("strong")[0].text

    # 5.3.1 关联企业自主核算并公开披露年度排放数据\
    CATI_5_3_1 = (
        soup1.find_all("div", {"class": "lists"})[16].find_all("strong")[1].text
    )

    # 5.3.2 关联企业自主设定并公开披露目标与进展
    CATI_5_3_2 = (
        soup1.find_all("div", {"class": "lists"})[16].find_all("strong")[2].text
    )

    # 5.4 减排行动-供应商企业自主开展碳管理 （总分：16.00）
    CATI_5_4 = soup1.find_all("div", {"class": "lists"})[17].find_all("strong")[0].text

    # 5.4.1 直接供应商自主核算并公开披露年度排放数据
    CATI_5_4_1 = (
        soup1.find_all("div", {"class": "lists"})[17].find_all("strong")[1].text
    )

    # 5.4.2 直接供应商自主设定并公开披露目标与进展
    CATI_5_4_2 = (
        soup1.find_all("div", {"class": "lists"})[17].find_all("strong")[2].text
    )

    # 5.4.3 间接供应商自主核算并公开披露年度排放数据
    CATI_5_4_3 = (
        soup1.find_all("div", {"class": "lists"})[17].find_all("strong")[3].text
    )

    # 5.4.4 间接供应商自主设定并公开披露目标与进展
    CATI_5_4_4 = (
        soup1.find_all("div", {"class": "lists"})[17].find_all("strong")[4].text
    )

    # 5.4.5 企业通过蔚蓝生态链或等效自动化系统赋能上游供应商开展供应链碳管理
    CATI_5_4_5 = (
        soup1.find_all("div", {"class": "lists"})[17].find_all("strong")[5].text
    )

    # 供应链（范围3）政策宣示 将供应商温室气体核算与报送纳入供应商行为准则
    Band_1 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[0].get("class")[0]
    )

    # 供应链（范围3）政策宣示 引导低碳、可持续消费，开展价值链减排
    Band_2 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[1].get("class")[0]
    )

    # 供应链（范围3）测算披露 测算并披露范围3排放量
    Band_3 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[2].get("class")[0]
    )

    # 供应链（范围3）测算披露 定期收集供应商实际排放数据
    Band_4 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[3].get("class")[0]
    )

    # 供应链（范围3）目标设定 设定并披露正在执行的范围3减排目标
    Band_5 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[4].get("class")[0]
    )

    # 供应链（范围3）目标设定 设定并披露范围3碳中和目标
    Band_6 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[5].get("class")[0]
    )

    # 供应链（范围3）目标设定 设定并披露的目标涵盖：推动供应商设定减排目标
    Band_7 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[6].get("class")[0]
    )

    # 供应链（范围3）目标绩效 披露范围3减排目标的完成进展
    Band_8 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[7].get("class")[0]
    )

    # 供应链（范围3）目标绩效 披露范围3碳中和目标的完成进展
    Band_9 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[8].get("class")[0]
    )

    # 供应链（范围3）目标绩效 通过蔚蓝生态链或等效自动化系统跟踪供应商目标设定的进展（至少包括在华供应商）
    Band_10 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[9].get("class")[0]
    )

    # 供应链（范围3）供应商企业自主开展碳管理 直接供应商自主核算并公开披露年度排放数据
    Band_11 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[10].get("class")[0]
    )

    # 供应链（范围3）供应商企业自主开展碳管理 直接供应商自主设定并公开披露目标与进展
    Band_12 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[11].get("class")[0]
    )

    # 供应链（范围3）供应商企业自主开展碳管理 间接供应商自主核算并公开披露年度排放数据
    Band_13 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[12].get("class")[0]
    )

    # 供应链（范围3）供应商企业自主开展碳管理 间接供应商自主设定并公开披露目标与进展
    Band_14 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[13].get("class")[0]
    )

    # 供应链（范围3）供应商企业自主开展碳管理 企业通过蔚蓝生态链或等效自动化系统赋能上游供应商开展供应链碳管理
    Band_15 = (
        soup2.find_all("ul", class_="manage-list")[0].find_all("p")[14].get("class")[0]
    )

    # 范围1+2 政策宣示 制定企业碳中和配套管理制度
    Band_16 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[0].get("class")[0]
    )

    # 范围1+2 测算披露 测算并披露范围1&2排放量
    Band_17 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[1].get("class")[0]
    )

    # 范围1+2 测算披露 测算并披露碳强度
    Band_18 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[2].get("class")[0]
    )

    # 范围1+2 目标设定 设定并披露正在执行的范围1&2减排目标
    Band_19 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[3].get("class")[0]
    )

    # 范围1+2 目标设定 设定并披露范围1&2碳中和目标
    Band_20 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[4].get("class")[0]
    )

    # 范围1+2 目标绩效 披露范围1&2减排目标的完成进展
    Band_21 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[5].get("class")[0]
    )

    # 范围1+2 目标绩效 披露范围1&2碳中和目标的完成进展
    Band_22 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[6].get("class")[0]
    )

    # 范围1+2 自身减排行动 开展非化石能源利用项目，并披露项目减排量
    Band_23 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[7].get("class")[0]
    )

    # 范围1+2 自身减排行动 开展能效提升技术应用项目，并披露项目减排量
    Band_24 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[8].get("class")[0]
    )

    # 范围1+2 自身减排行动 开展能源监测和管理项目
    Band_25 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[9].get("class")[0]
    )

    # 范围1+2 自身减排行动 通过碳抵消机制减排，并披露项目减排量
    Band_26 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[10].get("class")[0]
    )

    # 范围1+2 自身减排行动 推动其自有工厂、下属子公司、门店等披露碳排放数据，且/或设定减排目标
    Band_27 = (
        soup2.find_all("ul", class_="manage-list")[1].find_all("p")[11].get("class")[0]
    )

    # 公司名称
    company_name = soup2.find_all("div", class_="content")[0].find_all("strong")[0].text

    # 公司区域
    company_area = soup2.find_all("div", class_="content")[0].find_all("strong")[1].text

    # 公司行业
    company_industry = (
        soup2.find_all("div", class_="content")[0].find_all("strong")[2].text
    )

    # 股票代码
    company_code = soup2.find_all("div", class_="content")[0].find_all("strong")[3].text

    return [
        company_name,
        company_area,
        company_code,
        company_industry,
        CITI,
        CITI_all_rank,
        CITI_trade_rank,
        CATI,
        CATI_all_rank,
        CATI_trade_rank,
        CITI_1,
        CITI_1_1,
        CITI_1_2,
        CITI_2,
        CITI_2_1,
        CITI_2_2,
        CITI_3,
        CITI_3_1,
        CITI_3_2_1,
        CITI_3_2_2,
        CITI_3_3,
        CITI_3_4,
        CITI_4,
        CITI_4_1,
        CITI_4_2,
        CITI_5,
        CITI_5_1,
        CATI_1_1,
        CATI_1_1_1,
        CATI_1_1_2,
        CATI_1_1_3,
        CATI_1_2,
        CATI_1_2_1,
        CATI_1_2_2,
        CATI_1_2_3,
        CATI_2_1,
        CATI_2_1_1,
        CATI_2_1_2,
        CATI_2_1_3,
        CATI_2_1_4,
        CATI_2_2,
        CATI_2_2_1,
        CATI_2_2_2,
        CATI_3_1,
        CATI_3_1_1,
        CATI_3_1_2,
        CATI_3_1_3,
        CATI_3_1_4,
        CATI_3_2,
        CATI_3_2_1,
        CATI_3_2_2,
        CATI_3_2_3,
        CATI_3_2_4,
        CATI_4_1,
        CATI_4_1_1,
        CATI_4_1_2,
        CATI_4_1_3,
        CATI_4_2,
        CATI_4_2_1,
        CATI_4_2_2,
        CATI_4_2_3,
        CATI_5_1,
        CATI_5_1_1,
        CATI_5_1_2,
        CATI_5_1_3,
        CATI_5_1_4,
        CATI_5_1_5,
        CATI_5_2,
        CATI_5_2_1,
        CATI_5_2_2,
        CATI_5_2_3,
        CATI_5_2_4,
        CATI_5_2_5,
        CATI_5_3,
        CATI_5_3_1,
        CATI_5_3_2,
        CATI_5_4,
        CATI_5_4_1,
        CATI_5_4_2,
        CATI_5_4_3,
        CATI_5_4_4,
        CATI_5_4_5,
        Band_1,
        Band_2,
        Band_3,
        Band_4,
        Band_5,
        Band_6,
        Band_7,
        Band_8,
        Band_9,
        Band_10,
        Band_11,
        Band_12,
        Band_13,
        Band_14,
        Band_15,
        Band_16,
        Band_17,
        Band_18,
        Band_19,
        Band_20,
        Band_21,
        Band_22,
        Band_23,
        Band_24,
        Band_25,
        Band_26,
        Band_27,
    ]


def main():
    columns = [
        "Company_name",
        "Company_area",
        "Company_code",
        "Company_industry",
        "CITI",
        "CITI_all_rank",
        "CITI_trade_rank",
        "CATI",
        "CATI_all_rank",
        "CATI_trade_rank",
        "CITI_1",
        "CITI_1_1",
        "CITI_1_2",
        "CITI_2",
        "CITI_2_1",
        "CITI_2_2",
        "CITI_3",
        "CITI_3_1",
        "CITI_3_2_1",
        "CITI_3_2_2",
        "CITI_3_3",
        "CITI_3_4",
        "CITI_4",
        "CITI_4_1",
        "CITI_4_2",
        "CITI_5",
        "CITI_5_1",
        "CATI_1_1",
        "CATI_1_1_1",
        "CATI_1_1_2",
        "CATI_1_1_3",
        "CATI_1_2",
        "CATI_1_2_1",
        "CATI_1_2_2",
        "CATI_1_2_3",
        "CATI_2_1",
        "CATI_2_1_1",
        "CATI_2_1_2",
        "CATI_2_1_3",
        "CATI_2_1_4",
        "CATI_2_2",
        "CATI_2_2_1",
        "CATI_2_2_2",
        "CATI_3_1",
        "CATI_3_1_1",
        "CATI_3_1_2",
        "CATI_3_1_3",
        "CATI_3_1_4",
        "CATI_3_2",
        "CATI_3_2_1",
        "CATI_3_2_2",
        "CATI_3_2_3",
        "CATI_3_2_4",
        "CATI_4_1",
        "CATI_4_1_1",
        "CATI_4_1_2",
        "CATI_4_1_3",
        "CATI_4_2",
        "CATI_4_2_1",
        "CATI_4_2_2",
        "CATI_4_2_3",
        "CATI_5_1",
        "CATI_5_1_1",
        "CATI_5_1_2",
        "CATI_5_1_3",
        "CATI_5_1_4",
        "CATI_5_1_5",
        "CATI_5_2",
        "CATI_5_2_1",
        "CATI_5_2_2",
        "CATI_5_2_3",
        "CATI_5_2_4",
        "CATI_5_2_5",
        "CATI_5_3",
        "CATI_5_3_1",
        "CATI_5_3_2",
        "CATI_5_4",
        "CATI_5_4_1",
        "CATI_5_4_2",
        "CATI_5_4_3",
        "CATI_5_4_4",
        "CATI_5_4_5",
        "Band_1",
        "Band_2",
        "Band_3",
        "Band_4",
        "Band_5",
        "Band_6",
        "Band_7",
        "Band_8",
        "Band_9",
        "Band_10",
        "Band_11",
        "Band_12",
        "Band_13",
        "Band_14",
        "Band_15",
        "Band_16",
        "Band_17",
        "Band_18",
        "Band_19",
        "Band_20",
        "Band_21",
        "Band_22",
        "Band_23",
        "Band_24",
        "Band_25",
        "Band_26",
        "Band_27",
    ]
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }
    df = pd.DataFrame(columns=columns)
    count = 0
    for index in tqdm(range(1, 1700)):
        url1 = base_url1 + str(index)
        url2 = base_url2 + str(index)
        res1 = requests.get(url1, headers=head)
        res2 = requests.get(url2, headers=head)
        if res1.status_code != 200 or res2.status_code != 200:
            break
        else:
            res1.encoding = "utf-8"
            res2.encoding = "utf-8"
            try:
                os.makedirs("./html/{}".format(index))
            except:
                pass
            with open("./html/{}/1.html".format(index), "w", encoding="utf-8") as f:
                f.write(res1.text)
            with open("./html/{}/2.html".format(index), "w", encoding="utf-8") as f:
                f.write(res2.text)
            soup1 = bs4.BeautifulSoup(res1.text, "html.parser")
            soup2 = bs4.BeautifulSoup(res2.text, "html.parser")
            try:
                data = parse_data(soup1, soup2)
                df.loc[len(df.index)] = data
                count += 1
            except:
                continue
    df.to_excel("data.xlsx", index=True)
    print("共完成{}个公司".format(count))


if __name__ == "__main__":
    main()
