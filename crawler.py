import requests
import json
from lxml import etree
import re

header = {
    "cookie":"browserid=330580891164136630; timezoneOffset=28800,0; recentapps=%7B%22289070%22%3A1765619211%2C%22105600%22%3A1765523567%7D; sessionid=485287da4b17facad578f7fc; app_impressions=289070@1_5_9__412|512032@1_5_9__412|1308090@1_5_9__412|512033@1_5_9__412|512034@1_5_9__412|512035@1_5_9__412|645400@1_5_9__412|645401@1_5_9__412|645402@1_5_9__412|1308090@1_5_9__405|2158250@1_5_9__405|1478300@1_5_9__405|645402@1_5_9__405|947510@1_5_9__405",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}
url_top = "https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/?cc=cn"
r_top = requests.get(url=url_top, headers=header)
# with open("html.html","w",encoding="utf-8") as f:
#     f.write(r_top.text)
html = etree.HTML(r_top.text)
price = html.xpath("//*[@id='game_area_purchase_section_add_to_cart_123215']/div[2]/div/div[1]/text()")
price = re.search(r'[\d.]+', price[0]).group()
print(price)  # 输出: 220.00
