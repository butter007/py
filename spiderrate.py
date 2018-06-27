from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
from selenium.webdriver.chrome.options import Options
import sqlite3
from lxml import html


def get_content(url, searchDate, type, page=1):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chromedriver = 'C:/Python36/Scripts/chromedriver.exe'
    browser = webdriver.Chrome(chromedriver, options=chrome_options)
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
    jserectDate = "$('input[type=hidden][name=erectDate]').attr('value',%s)" % searchDate
    jsnothing = "$('input[type=hidden][name=nothing]').attr('value',%s)" % searchDate
    jspage = "$('input[type=hidden][name=page]').attr('value',%s)" % page
    jspjname = "$('input[type=hidden][name=pjname]').attr('value',%s)" % type
    browser.execute_script(jserectDate)
    browser.execute_script(jsnothing)
    browser.execute_script(jspage)
    browser.execute_script(jspjname)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "list_navigator")))
    browser.execute_script(jsformsubmit)
    print(browser.page_source)
    return browser.page_source


def getPage(content):
    pat = re.compile('m_nRecordCount = \d+')
    li = pat.findall(content)
    if li:
        mcounts = li[0].split()[2]
    pages = int(mcounts) // 20 + 1
    etree = html.etree
    htmlcon = etree.HTML(content)
    result = htmlcon.xpath('//div[@class="BOC_main publish"]/table/tr/td/text()')
    datalist = [result[i:i + 8] for i in range(0, len(result), 8)]
    if len(datalist[-1]) < 8:
        datalist.pop()
    print(datalist)
    return pages


if __name__ == '__main__':
    url = 'http://srh.bankofchina.com/search/whpj/search.jsp'
    content = get_content(url, '2018-6-13', '1316')
    page = getPage(content)
    con = sqlite3.connect('e:/mydatabase.db3')
    cur = con.cursor()
    cur.execute("""CREATE TABLE rate (
                                id INTERGER PRIMARY KEY,
                                name VARCHAR(40),
                                currencybuy FLOAT,
                                cashbuy FLOAT,
                                currencysell FLOAT,
                                cashbuy FLOAT,
                                cbankprice FLOAT,
                                publishdate VARCHAR(20),
                                publishtime VARCHAR(20))""")

