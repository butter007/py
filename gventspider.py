import requests
import gevent
from lxml import html
from gevent import monkey, pool
import re


def getFirstPage(url, startdate, enddate, currencycode):
    values = {'erectDate': startdate, 'nothing': enddate, 'pjname': currencycode}
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, data=values)
    if r.status_code == 200:
       content = r.text
    pat = re.compile('m_nRecordCount = \d+')
    li = pat.findall(content)
    if li:
        mcounts = li[0].split()[2]
    pages = int(mcounts) // 20 + 1
    return pages


def getContet(url, startdate, enddate, currencycode, page):
    values = {'erectDate': startdate, 'nothing': enddate, 'pjname': currencycode, 'page': page}
    r = requests.get(url)
    if r.status_code == 200:
        etree = html.etree
        htmlcon = etree.HTML(r.text)
        result = htmlcon.xpath('//div[@class="BOC_main publish"]/table/tr/td')


if __name__ == '__main__':
    url = 'http://srh.bankofchina.com/search/whpj/search.jsp'
    startdate = '2001-01-01'
    enddate = '2017-12-31'
    currencycode = '1316'
    pages = getFirstPage(url, startdate, enddate, currencycode)
    print(pages)
