#!/usr/bin/env python
# encoding: utf-8
'''
@author: Archer
@license: (C) Copyright 2018-2019, Node Supply Chain Manager Corporation Limited.
@contact: 347420070@qq.com
@software: garner
@file: youdao.py
@time: 2019/6/2 1:19
@desc:
'''
# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
import json

reload(sys)
sys.setdefaultencoding('utf-8')

YOUDAO_URL = 'http://openapi.youdao.com/api'
APP_KEY = '5cc343a5138aad9d'
APP_SECRET = '8iGRwtrL5ex2CKDzhJeAaXQdfynUvCBQ'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(s):
    q = s

    data = {}
    data['from'] = 'auto'
    data['to'] = 'auto'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    r = json.loads(response.content)
    result = ','.join(r['translation'])
    basic = ','.join(r['basic']['explains'])

    content = """
    结果：%s，
    解释：%s
    """ % (result, basic)

    print content


if __name__ == '__main__':
    connect("test")
