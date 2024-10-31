from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)

# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
# en_article_count = driver.find_element("css selector", "#articlecount > a:nth-child(1)")
# en_article_count.click()

driver.get("http://secure-retreat-92358.herokuapp.com/")
input_field = driver.find_element("class name", "form-control")
input_field.send_keys("James", Keys.TAB, "MacPherson", Keys.TAB, "email@example.com", Keys.RETURN)
