from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def page_init():
    driver.find_element("class name", "fc-primary-button").click()
    driver.implicitly_wait(2)
    driver.find_element("class name", "cc_btn_accept_all").click()
    driver.implicitly_wait(2)
    driver.find_element("id", "langSelect-EN").click()
    driver.implicitly_wait(2)


chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")
page_init()

cookie = driver.find_element("id", "bigCookie")
ame_aids = driver.find_elements("class name", "product")
