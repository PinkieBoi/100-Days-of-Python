import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def cookie_consent():
    driver.find_element(By.CLASS_NAME, "fc-primary-button").click()
    time.sleep(10)
    driver.find_element(By.CLASS_NAME, "cc_btn_accept_all").click()
    time.sleep(10)
    driver.find_element(By.ID, "langSelect-EN").click()
    time.sleep(10)


def click_cookie():
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()


def activate_helper():
    helpers = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    if len(helpers) > 0:
        helpers[-1].click()


chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")
cookie_consent()

timeout = time.time() + 5
five_mins = time.time() + 60 * 5

while True:
    click_cookie()

    if time.time() > timeout:
        activate_helper()
        timeout = time.time() + 5

    if time.time() > five_mins:
        c_per_sec = driver.find_element(By.ID, "cookiesPerSecond").text
        print(c_per_sec)
        break
