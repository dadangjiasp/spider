#!/usr/bin/python
# coding: utf-8

import requests
import json

def getjson(loc):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
    pa = {
        'q':'park', 
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': 0, 
        'output': 'json',
        'ak': 'DDtVK6HPruSSkqHRj5gTk0rc'
    }
    r = requests.get("http://api.map.baidu.com/place/v2/search", params=pa, headers= headers)
    decodejson = json.loads(r.text)
    print(r.text)
    return decodejson

getjson('shanghai')