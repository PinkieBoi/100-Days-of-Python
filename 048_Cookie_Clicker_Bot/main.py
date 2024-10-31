import time
from selenium import webdriver


def page_init():
    driver.find_element("class name", "fc-primary-button").click()
    time.sleep(2)
    driver.find_element("class name", "cc_btn_accept_all").click()
    time.sleep(2)
    driver.find_element("id", "langSelect-EN").click()
    time.sleep(2)


chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")
page_init()

cookie = driver.find_element("id", "bigCookie")
game_aids = driver.find_elements("id", "products")

while True:
    for item in game_aids[:5]:
        pass
    cookie.click()

driver.quit()
