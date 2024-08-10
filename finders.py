from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

bot = webdriver.Edge()
configuracao = webdriver.EdgeOptions()
configuracao.add_argument("--start-maximized")
bot = webdriver.Edge(options=configuracao)

bot.get("https://www.riotgames.com/pt-br")
bot.implicitly_wait(3)

#class_name
class_name_finder = bot.find_element(By.CLASS_NAME,"desktop-link-item").text
print("-----------------------------------------------------------------------------------------------------------")
print (class_name_finder)

#partial link text
partial_link_text_finder = bot.find_element(By.PARTIAL_LINK_TEXT, "JOGUE").text
print("-----------------------------------------------------------------------------------------------------------")
print (partial_link_text_finder)


#tag_name
tag_name_finder = bot.find_elements (By.TAG_NAME, "div")
print("-----------------------------------------------------------------------------------------------------------")
for i in tag_name_finder:
	print (i)

#xpath
botao = bot.find_element (By.XPATH, "//*[@data-riotbar-link-id= 'login'] [text() = 'Fazer Login']") #usando Selenium #tem que ser aspas simples (vem com aspas duplas)
botao.click()
print (botao)
sleep (5)

quit()