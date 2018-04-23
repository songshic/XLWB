# -*- coding: utf-8 -*-
import json
import re
import scrapy
from scrapy import Request,FormRequest
from urllib.parse import urlencode

from xinlangweibo.items import XlweiboItem


class XlweiboSpider(scrapy.Spider):
    name = 'xlweibo'
    allowed_domains = ['m.weibo.cn']
    search_url = 'https://m.weibo.cn/api/container/getIndex?'
    max_page = 3
    def start_requests (self):
        for page in range(1,self.max_page):
            data = {
                'type':'wb',
                'luicode':'10000011',
                'lfid':'100103type=1&q=电影',
                'queryVal':'热门电影',
                'containerid':'100103type=2&q=热门电影,',
                'page':page
            }
            url = self.search_url+urlencode(data)
            print(url)
            yield Request(url,callback = self.parse_index)


    def parse_index(self,response):
        html = json.loads(response.text)
        for item  in  html['data']['cards']:#遍历列表
            if isinstance(item,dict):#判断如果是字典
                for scheme in item['card_group']:#遍历列表，此时列表中的都为字典对象
                    yield  Request(scheme.get('scheme'),callback=self.parse_detail)


    def parse_detail(self,response):
        url= response.url
        if response.status == 200:
            if 'retweeted_status' in response.text:
                retweeted_status_text = re.search('("retweeted_status".*?"text".*?"(.*?))​",',response.text,re.S).group(2)
            else :
                retweeted_status_text = '原创'
            created_at = re.search('(status.*?created_at.*?:.*?"(.*?))",',response.text,re.S).group(2)
            text = re.search('"(status".*?"text".*?"(.*?))",',response.text,re.S).group(2)
            source = re.search('("status".*?"source".*?"(.*?))",',response.text,re.S).group(2)
            screen_name = re.search('(status.*?user.*?screen_name.*?:.*?"(.*?))",',response.text,re.S).group(2)
            weibo_items = XlweiboItem()
            for field in weibo_items.fields:
                try:
                    weibo_items[field] = eval(field) #动态获取定义的
                except NameError:
                    print('not defiend')
            yield weibo_items



