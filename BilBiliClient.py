#!/usr/bin/env python
# coding=utf-8
'''
> File Name: BilBiliClient.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  2/27 19:29:57 2019
'''

import requests

from config import config
class BilibiliClient():
    def __init__(self, av='', cookie=''):
        self.av=av
        self.cookie=cookie

    @property
    def headers(self):
        return {
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': self.cookie,
                'Origin': 'https://www.bilibili.com',
                'Referer': 'https://passport.bilibili.com/login'
        }

    def test_connection(self, url='https://api.bilibili.com/x/v1/dm/list.so?oid=26571968'):
        r = requests.get(url, headers=self.headers)
        print(r)

    def start_monitor(self, url='https://api.bilibili.com/x/v1/dm/list.so?oid=26571968'):
        pass

if __name__ == "__main__":
    b = BilibiliClient(cookie=config.COOKIE)
    b.test_connection()
