from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
from time import sleep

print ("\nPARTE 1------------------------------------------------------------------------\n")
configuracao = webdriver.EdgeOptions()
configuracao.add_argument("--start-maximized")
#configuracao.add_argument("--headless") #para rodar em segundo plano sem abrir o navegador
navegador = webdriver.Edge(options=configuracao)

navegador.get ("https://www.amazon.com.br/")
#navegador.delete_all_cookies()
sleep (2)

titulo = navegador.title
if titulo != "Amazon.com.br | Tudo pra você, de A a Z.":
	print ("Captcha")
	quit()

pesquisa = navegador.find_element (By.XPATH, "//input[@name= 'field-keywords']")
pesquisa.send_keys("One Piece 3 em 1")
pesquisa.submit()

print ("\nPARTE 2------------------------------------------------------------------------\n")
sleep (15)
navegador.save_screenshot('captura.jpg') #faz um screenshot da tela

pagina_atual = soup (navegador.page_source, 'html.parser')

nomes = pagina_atual.find_all ("span", class_= "a-size-base-plus")
precos = pagina_atual.find_all ("span", class_= "a-offscreen")
#link = item.find ("a", class_= "").get_text()
#frete = item.find ("span", class_= "a-color-base").get_text() - para exibir o frete verdadeiro tem de estar logado no site

for i in nomes:
	print (i.get_text())

print ("\nPARTE 3------------------------------------------------------------------------\n")
lista_nomes = []
lista_precos = []
volumes = {}

#Adicionar na lista
x = 0
for l in nomes:
	if 'ONE PIECE 3 EM 1' in nomes[x].get_text().upper() or 'ONE PIECE (3 EM 1)' in nomes[x].get_text().upper():
		lista_nomes.append (nomes [x].get_text())
		lista_precos.append(precos [x].get_text())
		volumes [lista_nomes[x]] = lista_precos [x]
	x += 1

#volumes = sorted (volumes)
for chave in volumes:
	print (chave)
	print (volumes[chave]) #valor da chave
	#print (nomes) #a Amazon tem exibido preços diferentes no site, mas quando clicar no produto verá que os valores exibido neste programa são verdadeiro

#imprimir na tela
for i in volumes:
	print (i)
	print(volumes[i])

#Adicionar na Planilha .csv
endereco = open ("armazenamento.csv", "w")
endereco.write ("VOLUMES,PRECOS\n")
for l in lista_nomes:
	endereco.write (f'{l},"{volumes[l]}"\n')
endereco.close()