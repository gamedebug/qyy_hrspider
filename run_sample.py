#!/usr/bin/env python3
# coding=utf-8
from liepin_spider import LiepinSpider
import sys
import xlwt
import  string
import pandas as pd
import codecs


spider = LiepinSpider()

url = 'https://www.liepin.com/zhaopin/?compIds=884492&ckid=f7fe680df72a13dc&fromSearchBtn=2&init=-1&sfrom=click-pc_homepage-centre_searchbox-search_new&flushckid=1&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&headckid=f7fe680df72a13dc&d_pageSize=40&siTag=LGV-fc5u_67LtFjetF6ACg~fA9rXquZc5IkJpXC-Ycixw&d_headId=b9ec8fc0c312e3c126e007a3872a082c&d_ckId=b9ec8fc0c312e3c126e007a3872a082c&d_sfrom=search_fp&d_curPage=0'

url_head = 'https://www.liepin.com/zhaopin/?compIds=884492&ckid=f7fe680df72a13dc&fromSearchBtn=2&init=-1&sfrom=click-pc_homepage-centre_searchbox-search_new&flushckid=1&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&headckid=f7fe680df72a13dc&d_pageSize=40&siTag=LGV-fc5u_67LtFjetF6ACg~fA9rXquZc5IkJpXC-Ycixw&d_headId=b9ec8fc0c312e3c126e007a3872a082c&d_ckId=b9ec8fc0c312e3c126e007a3872a082c&d_sfrom=search_fp&d_curPage='

def excel_write(items,index):
    for item in items:
        for i in range(0,5):
            ws.write(index,i,item[i])
        print(index)
        index+=1


newTable="results.xls"
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

xd = pd.ExcelFile('results.xls')
df = xd.parse()
with codecs.open('results.html','w','gb2312') as html_file:
        html_file.write(df.to_html(header = True,index = False))
