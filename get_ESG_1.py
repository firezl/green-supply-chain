import requests

url = "https://esg.api.ccxgf.com/common/esgCompanySearch?name=椰树"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
