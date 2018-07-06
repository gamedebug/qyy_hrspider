# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Executable script, created by
# Louis (luyisi@1000cc.net) on Sat Jul  7 1:32:26 2018.

#!/usr/bin/env python3
# coding=utf-8
from liepin_spider import LiepinSpider
import sys
import xlwt
import  string
import pandas as pd
import codecs


spider = LiepinSpider()

url = 'https://www.liepin.com/zhaopin/?pubTime=&ckid=503fd36933026680&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&dqs=&industryType=&jobKind=&sortFlag=15&degradeFlag=0&industries=&salary=&compscale=&key=Linux&clean_condition=&headckid=503fd36933026680&d_pageSize=40&siTag=7cnwpaXVd5e_aONzZHQ4MQ~fA9rXquZc5IkJpXC-Ycixw&d_headId=d5aaad8a9e4109a2682db2e5e7b0a2e6&d_ckId=d5aaad8a9e4109a2682db2e5e7b0a2e6&d_sfrom=search_prime&d_curPage=0&curPage=0'

url_head = 'https://www.liepin.com/zhaopin/?pubTime=&ckid=503fd36933026680&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&dqs=&industryType=&jobKind=&sortFlag=15&degradeFlag=0&industries=&salary=&compscale=&key=Linux&clean_condition=&headckid=503fd36933026680&d_pageSize=40&siTag=7cnwpaXVd5e_aONzZHQ4MQ~fA9rXquZc5IkJpXC-Ycixw&d_headId=d5aaad8a9e4109a2682db2e5e7b0a2e6&d_ckId=d5aaad8a9e4109a2682db2e5e7b0a2e6&d_sfrom=search_prime&d_curPage=0&curPage='

def excel_write(items,index):
    for item in items:
        for i in range(0,5):
            ws.write(index,i,item[i])
        print(index)
        index+=1


newTable="sample.xls"
wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('sheet1')
headData = ['职位', '链接', '薪资', '发布时间', '公司']

for colnum in range(0, 5):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))

index = 1
items = []
for page_num in range(0, spider.page_num(url)):
    url = url_head + str(page_num)
    items += spider.get(spider.get_content(url))

excel_write(items,index)
wb.save(newTable)

xd = pd.ExcelFile('sample.xls')
df = xd.parse()
with codecs.open('sample.html','w','gb2312') as html_file:
        html_file.write(df.to_html(header = True,index = False))
