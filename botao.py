from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Edge()
navegador.get("https://www.palavrasaleatorias.com/index.php")
navegador.implicitly_wait (0.5)

endereco_botao = navegador.find_element (by=By.NAME, value="Submit")
endereco_botao.click()
sleep(5)

driver.quit()