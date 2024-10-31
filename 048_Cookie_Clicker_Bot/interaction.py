from selenium import webdriver

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

en_article_count = driver.find_element("css selector", "#articlecount > a:nth-child(1)")
en_article_count.click()

# driver.quit()
