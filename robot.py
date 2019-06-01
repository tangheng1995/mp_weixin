#!/usr/bin/env python
# encoding: utf-8
'''
@author: Archer
@license: (C) Copyright 2018-2019, Node Supply Chain Manager Corporation Limited.
@contact: 347420070@qq.com
@software: garner
@file: robot.py
@time: 2019/6/2 1:11
@desc:
'''
import requests
import json
from youdao import connect

def get_turing_response(req=""):
    url = "http://www.tuling123.com/openapi/api"
    secretcode = "嘿嘿，这个就不说啦"
    response = requests.post(url=url, json={"key": secretcode, "info": req, "userid": 12345678})
    return json.loads(response.text)['text'] if response.status_code == 200 else ""


def get_qingyunke_response(req=""):
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(req)
    response = requests.get(url=url)
    return json.loads(response.text)['content'] if response.status_code == 200 else ""


# 简单做下。后面慢慢来
def get_response_by_keyword(keyword):
    if '关于' in keyword or 'about' in keyword:
        items = [
                 {"title": "我的博客", "description": "有时间写写",
                  "picurl": "http://p1.music.126.net/dpMCCy-yNxa0I5ZsmFZK9Q==/7869204721029611.jpg?param=180y180",
                  "url": "http://blog.heygolang.cn"}
                 ]
        result = {"type": "news", "content": items}
    else:
        content = connect(keyword)
        result = {"type": "text", "content": content}
    return result
