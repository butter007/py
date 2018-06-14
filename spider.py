# -*- encoding: utf-8 -*-
from lxml import etree
import urllib2
import urllib
import re
import time
import collections
import datetime


def get_url(url):
    url_list = []
    for i in range(1, 100):
        url_new = url + str(i)
        url_list.append(url_new)
    return url_list


def get_content(values, url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(url=url, data=data, headers=headers)
    res = urllib2.urlopen(req)
    content = res.read()
    return content.decode('utf-8')


def get_list(url, date, currencycode, page):
    values = {'erectDate': date, 'nothing': date, 'pjname': currencycode, 'page': page}
    content = get_content(values, url)
    pat = re.compile('m_nRecordCount = \d+')
    li = pat.findall(content)
    if li:
        mcounts = li[0].split()[2]
    pages = int(mcounts.encode('utf-8')) / 20 + 1
    html = etree.HTML(content)
    result = html.xpath('//div[@class="BOC_main publish"]/table/tr/td/text()')

    datalist = [result[i:i + 8] for i in range(0, len(result), 8)]
    if len(datalist[-1]) < 8:
        datalist.pop()
    return datalist, pages


def getdatalistindex(datalist, standtime):
    # standbefo = '2019.02.09 08:25:00'
    # standtime = '2018.02.09 09:00:00'
    # timeafter = '2018.02.09 09:24:00'

    timeArray = time.strptime(standtime, '%Y.%m.%d %H:%M:%S')
    timestamp = time.mktime(timeArray)
    index = 0
    for i, val in enumerate(datalist):
        tArray = time.strptime(val[7], '%Y.%m.%d %H:%M:%S')
        tstamp = time.mktime(tArray)
        timelast = timestamp - tstamp
        if timelast > 0:
            timeafter = time.strptime(datalist[i - 1][7], '%Y.%m.%d %H:%M:%S')
            timeafterstamp = time.mktime(timeafter)
            timeinterval = timeafterstamp - timestamp
            if timelast > timeinterval:
                index = i - 1
            else:
                index = i
            return index
    return index


def getmoneyrate(url, code, standtime, date):
    datalist, pages = get_list(url, date, code, 1)
    index = getdatalistindex(datalist, standtime)
    if index == 0:
        for i in range(1, pages + 1):
            datalist, pages = get_list(url, date, code, i)
            index = getdatalistindex(datalist, standtime)
            if index != 0:
                return datalist[index][1]


if __name__ == '__main__':
    url = 'http://srh.bankofchina.com/search/whpj/search.jsp'
    dt = datetime.datetime.now()
    date = dt.strftime('%Y-%m-%d')
    standtime = dt.strftime('%Y.%m.%d') + ' 09:00:00'

    # standtime = '2018.02.12 09:00:00'
    # date = '2018-02-12'
    currencycode = collections.OrderedDict()

    currencycode['CHF'] = 1317
    currencycode['AUD'] = 1325
    currencycode['HKD'] = 1315
    currencycode['GBP'] = 1314
    currencycode['EUR'] = 1326
    currencycode['JPY'] = 1323
    currencycode['USD'] = 1316
    li = []
    with open('rate.txt', 'a+') as f:
        for data in f:
            if data:
                li.append(data)

    with open('rate.txt', 'w') as f:
        for key, val in currencycode.items():
            line_data = key + ':' + getmoneyrate(url, val, standtime, date) + '\n'
            li.insert(0, line_data)
        li.insert(0, '----------------------------'+date+'-----------------------------\n')
        for txt_line_data in li:
            if txt_line_data:
                f.write(txt_line_data)
