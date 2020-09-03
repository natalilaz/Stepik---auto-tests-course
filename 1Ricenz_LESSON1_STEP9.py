from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@class='form-control first']")
    input1.send_keys("I")
    input2 = browser.find_element_by_xpath("//input[@class='form-control second']")
    input2.send_keys("Pev")
    input3 = browser.find_element_by_xpath("//input[@class='form-control third']")
    input3.send_keys("Ssk")
    input4 = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
    input4.send_keys("3")
    input5 = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    input5.send_keys("R")
    button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

