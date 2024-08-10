from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

configuracao = webdriver.EdgeOptions()
configuracao.add_argument("--start-maximized")
#configuracao.add_argument("--headless") #para rodar em segundo plano sem abrir o navegador
navegador = webdriver.Edge(options=configuracao)

link = "https://www.amazon.com.br/"
site = navegador.get (link)
sleep (2)

pesquisa = navegador.find_element (By.XPATH, "//input[@name= 'field-keywords']")
pesquisa.send_keys("One Piece 3 em 1")
pesquisa.submit()
sleep (4)

lista_geral = []

preco = navegador.find_elements(By.XPATH, "//span[@class = 'a-price-whole']")
for i in preco:
	a = i.text
	p = int (a)
	if p < 60:
		lista_geral.append(p)

for g in lista_geral:
	print (g)

#geral = navegador.find_elements (By.XPATH, "//div[@class= 'a-spacing-base']")