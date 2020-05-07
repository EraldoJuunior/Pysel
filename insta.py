from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/?hl=pt-br")
elem = browser.find_element_by_name("username")

elem.send_keys("ll")

elem.submit()



