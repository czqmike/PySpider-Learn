# -*- coding:utf-8 -*-
# 这是一个自动从百度图片上爬输入关键词的图片的脚本，图片默认保存在【F:\picture\你输入的关键字】下
import re
import requests
import os

def downloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)

    # 创建文件夹并且将cur_dir修改为下载路径
    cur_dir = "F:\picture"      # 默认工作路径，如果找不到则下载到当前路径的keyword文件夹下
    if not os.path.isdir(cur_dir):
        cur_dir = os.curdir
    os.mkdir(os.path.join(cur_dir, keyword))
    cur_dir += '\\' + keyword + '\\'

    # 用匹配到的URL下载图片
    i = 1
    for each in pic_url:
        print("Downloading " + str(i) + "st picture, the URL is:" + str(each))
        try:
            pic = requests.get(each, timeout = 10)
        except requests.exceptions.ConnectionError:
            print("Time out, next picture is going to download.")
            continue
        string = cur_dir + keyword + '_' + str(i) + ".jpg"
        fp = open(string, "wb")
        fp.write(pic.content)
        fp.close()
        i += 1


word = input("please input key words:")
url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&" \
      'word=' + word + '&ct=201326592&ic=0&lm=-1&width=&height=&v=flip'
result = requests.get(url)
downloadPic(result.text, word)
