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

import urllib.request
import re


class LiepinSpider:

    def get_content(self, url):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                   AppleWebKit/537.36 (KHTML, like Gecko)'
                   'Chrome/51.0.2704.63 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def get(self, html):

        reg = '<h3 title=".*?">.*?<a href="(.*?)".*?'
        reg += '>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t(.*?)</a>.*?</h3>.*?'
        reg += '<span class="text-warning">(.*?)</span>.*?'
        reg += '<time title="(.*?)">.*?</time>.*?'
        reg += '<a title="公司(.*?)"'
        reg = re.compile(reg, re.S)
        items = re.findall(reg, html)
        return items

    def page_num(self, url):

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/51.0.2704.63 Safari/537.36'}
        req = urllib.request.Request(url=url,headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        reg = re.compile(r'<a class="last" href=".*curPage=(.*?)" title="末页">',re.S)
        items = re.findall(reg,html)
        page_num = int(items[0])
        return page_num
