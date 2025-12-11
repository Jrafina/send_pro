import requests
import  json
import  pprint
from lxml import etree

header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
    }
print("*"*25+"以下是热搜"+"*"*25)
url_top = "https://api.rebang.today/v1/items?tab=top&sub_tab=today&page=1&version=1"
r_top = requests.get(url = url_top,headers=header)
list1 = r_top.json()["data"]["list"]
data = json.loads(list1)
# pprint.pprint(data)
desc_list = [item.get("desc", "") for item in data][:3]
url_list = [item.get("www_url", "") for item in data][:3]
dic1 = dict(zip(desc_list,url_list))

for desc,url in dic1.items():
    print(desc+url +"\n")


print("*"*25+"以下是天气"+"*"*25)
url = "https://www.weather.com.cn/weather/101270102.shtml"
r = requests.get(url=url,headers=header)
r.encoding = r.apparent_encoding
html = etree.HTML(r.text)
weather = html.xpath("//*[@id='7d']/ul/li[1]/p[1]/text()")[0]
tem = html.xpath("//*[@id='7d']/ul/li[1]/p[2]/i/text()")[0]
today_tem_whe = f"今天的天气是 {weather} ,温度是 {tem}"
print(today_tem_whe)