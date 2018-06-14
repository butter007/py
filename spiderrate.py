from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


def get_content(url):
    chromedriver = 'C:/Python36/Scripts/chromedriver.exe'
    browser = webdriver.Chrome(chromedriver)
    browser.get(url)
    initial_time_input_tag = browser.find_element_by_name('erectDate')
    jserectDate = "$('input[name=erectDate]').attr('readonly',false)"
    jsnothing = "$('input[name=nothing]').attr('readonly',false)"

    browser.execute_script(jserectDate)
    browser.execute_script(jsnothing)
    initial_time_input_tag.send_keys('2018-06-13')
    terminal_time_input_tab = browser.find_element_by_name('nothing')
    terminal_time_input_tab.send_keys('2018-06-13')
    currency_selectinput_tag = Select(browser.find_element_by_name('pjname'))
    currency_selectinput_tag.select_by_value('1316')
    browser.find_elements_by_class_name('search_btn')[1].click()
    print(browser.page_source)


    wait = WebDriverWait(browser, 10)

    wait.until(EC.presence_of_element_located((By.ID,"list_navigator")))


if __name__ == '__main__':
    url = 'http://srh.bankofchina.com/search/whpj/search.jsp'
    get_content(url)