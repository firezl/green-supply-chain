import pandas as pd
import numpy as np
import patsy
import statsmodels.api as sm

# 读取数据
data = pd.read_excel("data/data_cn_lc.xlsx")

# 数据处理
score = {
    "na": 0,
    "B": 1,
    "BB": 2,
    "BBB-": 3,
    "BBB": 4,
    "BBB+": 5,
    "A-": 6,
    "A": 7,
    "AA-": 8,
    "AA": 9,
    "A+": 10,
}
data["ESG_ccxi"] = data["ESG_ccxi"].fillna("na").apply(lambda x: score[x])


# def re_histogram(esg):
#     hist = []
#     for i in range(0, int(esg.max()) + 1):
#         hist = np.append(hist, np.sum(esg == i))
#     re_hist = np.zeros(5)
#     re_dict = {}
#     partition = np.round(hist.sum() / 5)
#     index = 0
#     for i, v in enumerate(hist):
#         if v <= partition - re_hist[index]:
#             re_hist[index] += v
#             re_dict[i] = index
#         else:
#             if v + re_hist[index] > partition * 1.2:
#                 index += 1
#                 if index == 5:
#                     index = 4
#                     re_hist[index] += v
#                     re_dict[i] = index
#                 else:
#                     re_hist[index] += v
#                     re_dict[i] = index
#             else:
#                 re_hist[index] += v
#                 re_dict[i] = index
#                 index += 1
#                 if index == 5:
#                     index = 4
#     return re_dict


# re_score = re_histogram(data["Environment"])
# data["Environment"] = data["Environment"].apply(lambda x: re_score[x])
ci_score = zip(
    data["Company_industry"].unique(), range(len(data["Company_industry"].unique()))
)
ci_score = dict(ci_score)
data["Company_industry"] = data["Company_industry"].apply(lambda x: ci_score[x])
data["CEmissReduce"] = data["CEmissReduce"].fillna(0).apply(lambda x: np.log10(x + 1))
data["CEmission"] = data["CEmission"].fillna(0).apply(lambda x: np.log10(x + 1))
data["SC_CC"] = data["SC_CC"].fillna(0)
data["SC_PC"] = data["SC_PC"].fillna(0)
data["SC_CCHHI"] = data["SC_CCHHI"].fillna(0)
data["SC_PCHHI"] = data["SC_PCHHI"].fillna(0)
data["SC_SCC"] = data["SC_SCC"].fillna(0)

# check
if pd.isnull(data["SC_CC"]).sum() != 0:
    print("SC_CC has nan")
if pd.isnull(data["SC_PC"]).sum() != 0:
    print("SC_PC has nan")
if pd.isnull(data["SC_CCHHI"]).sum() != 0:
    print("SC_CCHHI has nan")
if pd.isnull(data["SC_PCHHI"]).sum() != 0:
    print("SC_PCHHI has nan")
if pd.isnull(data["SC_SCC"]).sum() != 0:
    print("SC_SCC has nan")

if pd.isnull(data["Environment"]).sum() != 0:
    print("Environment has nan")
if pd.isnull(data["Company_industry"]).sum() != 0:
    print("Company_industry has nan")
if pd.isnull(data["CITI"]).sum() != 0:
    print("CITI has nan")
if pd.isnull(data["CITI_all_rank"]).sum() != 0:
    print("CITI_all_rank has nan")
if pd.isnull(data["CITI_trade_rank"]).sum() != 0:
    print("CITI_trade_rank has nan")
if pd.isnull(data["CATI"]).sum() != 0:
    print("CATI has nan")
if pd.isnull(data["CATI_all_rank"]).sum() != 0:
    print("CATI_all_rank has nan")
if pd.isnull(data["CATI_trade_rank"]).sum() != 0:
    print("CATI_trade_rank has nan")
if pd.isnull(data["CEmissReduce"]).sum() != 0:
    print("CEmissReduce has nan")
if pd.isnull(data["CEmission"]).sum() != 0:
    print("CEmission has nan")

index = np.random.choice(range(len(data)), size=len(data), replace=False)
train_index = index[: int(len(data) * 0.5)]
test_index = index[int(len(data) * 0.5) :]
train = data.iloc[train_index]
test = data.iloc[test_index]

y, X = patsy.dmatrices(
    "ESG_ccxi ~ Company_industry + CITI + CITI_all_rank + CITI_trade_rank + CATI + CATI_all_rank + CATI_trade_rank + CEmissReduce + CEmission + SC_CC + SC_PC + SC_CCHHI + SC_PCHHI + SC_SCC",
    data=train,
    return_type="dataframe",
)

model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

y_test, X_test = patsy.dmatrices(
    "ESG_ccxi ~ Company_industry + CITI + CITI_all_rank + CITI_trade_rank + CATI + CATI_all_rank + CATI_trade_rank + CEmissReduce + CEmission + SC_CC + SC_PC + SC_CCHHI + SC_PCHHI + SC_SCC",
    data=test,
    return_type="dataframe",
)

y_pred = results.predict(X_test)
y_pred = np.round(y_pred)
y_test = y_test["ESG_ccxi"].values
print("test accuracy: ", np.sum(y_pred == y_test) / len(y_test))
