import requests
import  json
import  pprint
from lxml import etree
import time

print("*"*12 + "以下是热搜"+"*"*12)
header = {
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
param = {"snr": "1_12_4__7", "term": "Sid Meier’s Civilization® VI"}
url_game = "https://store.steampowered.com/search"
success = False
for i in range(3):
    try:
        r_game = requests.get(url=url_game, headers=header, params=param, timeout=10)
        html = etree.HTML(r_game.text)
        price = html.xpath('//div[@class="discount_final_price"][1]/text()')[0].strip()
        name = html.xpath('//div[@class = "responsive_search_name_combined"][1]//span/text()')[0].strip()
        print(f"{name}的价格是：{price}")
        success = True
        break
    except:
        if i < 2:
            time.sleep(1)
            continue
if not success:
    print("错误输出，请检查程序")