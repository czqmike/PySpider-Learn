# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.hbue.edu.cn"
response = requests.get(url)
response.encoding = 'utf-8'     #使用utf-8重新编码，防止乱码
html = response.text

soup = BeautifulSoup(html, "html.parser")
result = soup.find(class_="wp_nav")             #得到总的ul

content_list = [[]]
for li in result.find_all(name='li', recursive=False):      #recursive获得直接子节点（不包括孙子往后的节点）
    temp_list = []
    temp_list.append(li.a.span.string)                  #每个列表放一栏的数据，先放入标题

    for sub in li.find_all(class_='sub-nav'):
        for li2 in sub.find_all(name='li'):
            temp_list.append(li2.a.span.string)         #对每个栏目进行填充
    content_list.append(temp_list)

with open('data.csv', 'w') as csvfile:                  #写入文件，一个一维列表对应一栏的数据
    writer = csv.writer(csvfile)
    for item in content_list:
        writer.writerow(item)
