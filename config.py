#!/usr/bin/env python
# coding=utf-8
'''
> File Name: config.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  2/27 19:59:37 2019
'''
import os

class Config():
    COOKIE = os.getenv("COOKIE")


config=Config()
