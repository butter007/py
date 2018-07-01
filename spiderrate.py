from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
from selenium.webdriver.chrome.options import Options
import sqlite3
from lxml import html
import time


def get_content(browser, url, searchDate, enddate, type, page=1):
    browser.get(url)
    #    initial_time_input_tag = browser.find_element_by_name('erectDate')
    #    jserectDate = "$('input[name=erectDate]').attr('readonly',false)"
    #    jsnothing = "$('input[name=nothing]').attr('readonly',false)"
    #    jspage = "$('input[name=page]').attr('value','2')"
    #    initial_page_input_tag = browser.find_element_by_xpath("//input[@name='page']")

    #    browser.execute_script(jserectDate)
    #    browser.execute_script(jsnothing)
    #    browser.execute_script(jspage)

    #    initial_time_input_tag.send_keys('2018-06-13')
    #    terminal_time_input_tab = browser.find_element_by_name('nothing')
    #    terminal_time_input_tab.send_keys('2018-06-13')
    #    currency_selectinput_tag = Select(browser.find_element_by_name('pjname'))
    #    currency_selectinput_tag.select_by_value('1316')
    #    browser.find_elements_by_class_name('search_btn')[1].click()
    jsformsubmit = "document.pageform.submit()"
    jserectDate = "$('input[type=hidden][name=erectDate]').attr('value',%s)" % ("'" + searchDate + "'")
    jsnothing = "$('input[type=hidden][name=nothing]').attr('value',%s)" % ("'" + enddate + "'")
    jspage = "$('input[type=hidden][name=page]').attr('value',%s)" % page
    jspjname = "$('input[type=hidden][name=pjname]').attr('value',%s)" % type
    browser.execute_script(jserectDate)
    browser.execute_script(jsnothing)
    browser.execute_script(jspage)
    browser.execute_script(jspjname)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "list_navigator")))
    browser.execute_script(jsformsubmit)
    return browser.page_source


def getPage(content):
    pat = re.compile('m_nRecordCount = \d+')
    li = pat.findall(content)
    if li:
        mcounts = li[0].split()[2]
    pages = int(mcounts) // 20 + 1
    etree = html.etree
    htmlcon = etree.HTML(content)
    result = htmlcon.xpath('//div[@class="BOC_main publish"]/table/tbody/tr/td/text()')
    datalist = [result[i:i + 8] for i in range(0, len(result), 8)]
    if len(datalist[-1]) < 8:
        datalist.pop()
    return datalist, pages


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chromedriver = 'C:/Python36/Scripts/chromedriver.exe'
    browser = webdriver.Chrome(chromedriver, options=chrome_options)
    now = lambda: time.time()
    start = now()
    url = 'http://srh.bankofchina.com/search/whpj/search.jsp'
    content = get_content(browser, url, '2001-01-01', '2017-12-31', '1316')
    datalist, pages = getPage(content)
    con = sqlite3.connect('e:/mydatabase.db3')
    cur = con.cursor()
    cur.execute("""CREATE TABLE rate (
                                id INTERGER PRIMARY KEY ,
                                name VARCHAR(30),
                                currencybuy FLOAT,
                                cashbuy FLOAT,
                                currencysell FLOAT,
                                cashsell FLOAT,
                                wgprice FLOAT,
                                cbankprice FLOAT,
                                publishdate VARCHAR(16),
                                publishtime VARCHAR(16)
                                )""")
    index = 1
    for dataitem in datalist:
        # print (datalist)
        datatimelist = dataitem[7].split()
        cur.execute("""INSERT INTO rate (id,name,currencybuy,cashbuy,currencysell,cashsell,wgprice,cbankprice,publishdate,publishtime)
              VALUES ('%d','%s','%f', '%f', '%f', '%f', '%f','%f','%s','%s' )""" % (
            index, dataitem[0], float(dataitem[1]), float(dataitem[2]), float(dataitem[3]), float(dataitem[4]),
            float(dataitem[5]),
            float(dataitem[6]),
            datatimelist[0], datatimelist[1]))
        index += 1
    for page in range(2, pages + 1):
        content = get_content(browser,url, '2001-01-01', '2017-12-31', '1316', page)
        datalist, abc = getPage(content)
        datatimelist = dataitem[7].split()
        for dataitem in datalist:
            cur.execute("""INSERT INTO rate (id,name,currencybuy,cashbuy,currencysell,cashsell,wgprice,cbankprice,publishdate,publishtime)
                 VALUES ('%d','%s','%f', '%f', '%f', '%f', '%f','%f','%s','%s' )""" % (
                index, dataitem[0], float(dataitem[1]), float(dataitem[2]), float(dataitem[3]), float(dataitem[4]),
                float(dataitem[5]), float(dataitem[6]), datatimelist[0], datatimelist[1]))
            index += 1
        con.commit()
    con.close()
    print("Time:", now() - start)
