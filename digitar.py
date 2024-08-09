from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge()
sleep (1)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
sleep (5)

text_box = driver.find_element(by=By.NAME, value="my-text")
text_box.send_keys("Isso aqui está digitando pra mim")
sleep(10)

driver.quit()