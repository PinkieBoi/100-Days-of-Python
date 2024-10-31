from selenium import webdriver

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)
driver.get(url="https://www.python.org")

events_dict = {}
events_section = driver.find_element("class name", "event-widget")
for event in events_section.find_elements("tag name", "li"):
    events_dict[len(events_dict)] = {
        "time": event.find_element("tag name", "time").text,
        "name": event.find_element("tag name", "a").text,
        "link": event.find_element("tag name", "a").get_property("href")
    }


driver.quit()

print(events_dict)
