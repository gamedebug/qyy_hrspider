# Copyright Yi-Si.Lu (luyisi1982@gmail.com)
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

from liepin_spider import LiepinSpider
import sys
import xlwt
import pandas as pd
import codecs


spider = LiepinSpider()

task_name = input("Input your task name: ")

url = input("Input the URL of search result page: ")

url_head = url[:-1]

excel_file = task_name + '.xls'

html_file = task_name + '.html'

def excel_write(items,index):
    for item in items:
        for i in range(0,5):
            ws.write(index,i,item[i])
        # print(index)
        index+=1


newTable="task_name.xls"
wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('sheet1')
headData = ['链接', '职位', '薪资', '发布时间', '公司']

for colnum in range(0, 5):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))

index = 1
items = []
for page_num in range(0, spider.page_num(url)):
    url = url_head + str(page_num)
    items += spider.get(spider.get_content(url))

excel_write(items,index)
wb.save(newTable)

xd = pd.ExcelFile(excel_file)
df = xd.parse()
with codecs.open(html_file,'w','utf-8') as html_file:
    html_file.write(df.to_html(header = True,index = False))

with open(html_file, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write('<meta charset="UTF-8">'+content)
