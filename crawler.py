import requests
import  json
import  pprint
from lxml import etree
import time
import re

print("*"*12 + "以下是热搜"+"*"*12)
header = {
    "Accept-Language": "zh-CN,zh;q=0.9",
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
    }

url_hotsearch = "https://api.rebang.today/v1/items?tab=top&sub_tab=today&page=1&version=1"
r_hotsearch = requests.get(url = url_hotsearch,headers=header)
list1 = r_hotsearch.json()["data"]["list"]
data = json.loads(list1)
# pprint.pprint(data)
desc_list = [item.get("desc", "") for item in data][:3]
url_list = [item.get("www_url", "") for item in data][:3]
dic1 = dict(zip(desc_list,url_list))

for desc,url in dic1.items():
    print(desc+url +"\n")


print("*"*12 + "以下是天气"+"*"*12)
url_weather = "https://www.weather.com.cn/weather/101270102.shtml"
r_weather = requests.get(url=url_weather,headers=header)
r_weather.encoding = r_weather.apparent_encoding
html = etree.HTML(r_weather.text)
weather = html.xpath("//*[@id='7d']/ul/li[1]/p[1]/text()")[0]
tem = html.xpath("//*[@id='7d']/ul/li[1]/p[2]/i/text()")[0]
today_tem_whe = f"今天的天气是 {weather} ,温度是 {tem}"
print(today_tem_whe)



print("*"*12 + "以下是查价"+"*"*12)
url_top = "https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/?cc=cn"
r_top = requests.get(url=url_top, headers=header)
# with open("html.html","w",encoding="utf-8") as f:
#     f.write(r_top.text)
html = etree.HTML(r_top.text)
price = html.xpath("//*[@id='game_area_purchase_section_add_to_cart_123215']/div[2]/div/div[1]/text()")
price = re.search(r'[\d.]+', price[0]).group()
name = html.xpath("//*[@id='appHubAppName']/text()")[0]
print(name + ":" +price+"元")  # 输出: 220.00
