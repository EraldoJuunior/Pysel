from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


username = "lk"
senha= "9"
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/?hl=pt-br")

sleep(5)

elem = browser.find_element_by_xpath('//input[@name="username"]')
elem.clear()

elem.send_keys(username)

elem = browser.find_element_by_xpath('//input[@name="password"]')
elem.clear()

elem.send_keys(senha)

elem.send_keys(Keys.ENTER)
sleep(5)

