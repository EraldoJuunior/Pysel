from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get("http://www.python.org")
elem = browser.find_element_by_id("id-search-field")
elem.send_keys('1')


elem.send_keys(Keys.ENTER)
elem.submit()

browser.close()

