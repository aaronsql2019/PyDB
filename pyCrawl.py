# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import json
import pprint
import re
import requests

r = requests.get('http://wwbc.com.tw/test/dhl/dhl_box/#1', timeout=3)
print('GET狀態碼: ', r.status_code)
# 強迫退出程式並取得錯誤內容
# raise HTTPError if status != 2XX
r.raise_for_status()

print(r.encoding, r.content)
r.encoding = 'utf-8'

html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')


name = []
# 找到所有class是black的span
for black in soup.find_all("span", class_="black"):
    # 過濾class black裡面的class grey
    if black.find(class_="grey"):
        continue
    name.append(black.get_text().strip())  # 只取字串
    # print('==========')
    # print(black.get_text().strip())

size = []
# 找到所有class是grey的span
for grey in soup.find_all("span", class_="grey"):
    size.append(grey.get_text().strip())  # 只取字串
    # print('==========')
    # print(grey.get_text().strip())

data = []
for d in range(len(name)):
    data.append({'name': name[d-1], 'size': size[d-1]})
pprint.pprint(data)

with open('boxes.json', 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4, sort_keys=True)
    print('已存到JSON檔')
