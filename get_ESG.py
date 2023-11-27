import requests
import json

url = "https://esg.api.ccxgf.com/common/esgRatingSearch?name=华为技术有限公司"

payload = {}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua": '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "Referer": "http://esgratings.ccxgf.com/",
    "Origin": "http://esgratings.ccxgf.com",
    "Host": "esg.api.ccxgf.com",
}

response = requests.request("GET", url, headers=headers, data=payload)
result = response.json()
response.close()
if result["msg"] == "请求成功":
    result = result["result"]
    print(result["data"]["companyName"])
    print(result["data"]["securityCode"])
    print(result["data"]["ratingLevel"])
    print(result["data"]["environment"])
    print(result["data"]["social"])
    print(result["data"]["governance"])
print(result)
