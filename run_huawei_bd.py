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

url = 'https://www.liepin.com/zhaopin/?pubTime=&ckid=52deb7a257216095&fromSearchBtn=2&compkind=&searchType=1&dqs=&compIds=954482&jobKind=&sortFlag=15&salary=&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&headckid=b477f3060083bfdc&isAnalysis=&init=-1&industryType=&degradeFlag=0&industries=&compscale=&clean_condition=&d_pageSize=40&siTag=LGV-fc5u_67LtFjetF6ACg~fA9rXquZc5IkJpXC-Ycixw&d_headId=a9a54a63b6466b81a581384304f1773f&d_ckId=a9a54a63b6466b81a581384304f1773f&d_sfrom=search_prime&d_curPage=0&curPage=0'

url_head = 'https://www.liepin.com/zhaopin/?pubTime=&ckid=52deb7a257216095&fromSearchBtn=2&compkind=&searchType=1&dqs=&compIds=954482&jobKind=&sortFlag=15&salary=&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&headckid=b477f3060083bfdc&isAnalysis=&init=-1&industryType=&degradeFlag=0&industries=&compscale=&clean_condition=&d_pageSize=40&siTag=LGV-fc5u_67LtFjetF6ACg~fA9rXquZc5IkJpXC-Ycixw&d_headId=a9a54a63b6466b81a581384304f1773f&d_ckId=a9a54a63b6466b81a581384304f1773f&d_sfrom=search_prime&d_curPage=0&curPage='

def excel_write(items,index):
    for item in items:
        for i in range(0,5):
            ws.write(index,i,item[i])
        # print(index)
        index+=1


newTable="huawei_bd.xls"
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

xd = pd.ExcelFile('huawei_bd.xls')
df = xd.parse()
with codecs.open('huawei_bd.html','w','utf-8') as html_file:
    html_file.write(df.to_html(header = True,index = False))

with open('huawei_bd.html', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write('<meta charset="UTF-8">'+content)
