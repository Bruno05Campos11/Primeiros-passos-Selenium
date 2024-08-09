#Raspagem simples
import requests
from bs4 import BeautifulSoup as bs

link = "https://www.bing.com/search?pglt=673&q=one+piece"
#para reconhecer como Edge
requests_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"}

requisicao = requests.get (link, headers = requests_headers)
print (requisicao)
#print (requisicao.text) - modo mais primitivo de imprimir conteúdo html
site = bs (requisicao.text,"html.parser")

'''pesquisa = site.find ("span") #função do Beautiful Soup para encontrar um elemento
pesquisa2 = site.find_all ("span") #retorna uma lista com todos os elementos com essa tag
print (pesquisa)
print (pesquisa2)
print (pesquisa2[6])'''

pesquisa3 = site.find ("textarea", class_ = "b_searchbox")
print (pesquisa3 ["value"])

pesquisa4 = site.find ("span", class_ = "wpt-ovn")
print (pesquisa4.get_text())