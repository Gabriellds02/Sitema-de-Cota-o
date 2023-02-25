import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from Google_Shopping.Google_Shopping import busca_google_shopping
from Buscape.buscape import buscape

df = pd.read_excel(r'J:\Meu Drive\Python - Treinamentos\Projeto Integração Web\Projeto de Integração Web\Data_frame\buscas.xlsx')
nav = webdriver.Chrome(executable_path= r'./chromedriver')

tabela_ofertas = pd.DataFrame()
for linha in df.index:
    produto = df.loc[linha, "Nome"]
    termos_banidos = df.loc[linha, "Termos banidos"]
    preco_minimo = df.loc[linha, "Preço mínimo"]
    preco_maximo = df.loc[linha, "Preço máximo"]
    
    lista_ofertas_google_shopping = busca_google_shopping(nav, produto, termos_banidos, preco_minimo, preco_maximo)
    if lista_ofertas_google_shopping:
        tabela_google_shopping = pd.DataFrame(lista_ofertas_google_shopping, columns=['produto', 'preco', 'link'])
        tabela_ofertas = tabela_ofertas.append(tabela_google_shopping)
    else:
        tabela_google_shopping = None
    
    time.sleep(2)
    lista_ofertas_buscape = buscape(nav, produto, termos_banidos, preco_minimo, preco_maximo)
    if lista_ofertas_buscape:
        tabela_buscape = pd.DataFrame(lista_ofertas_buscape, columns=['produto', 'preco', 'link'])
        tabela_ofertas = tabela_ofertas.append(tabela_buscape)
    else:
        tabela_buscape = None

display(tabela_ofertas)
tabela_ofertas.to_excel('ofertas.xlsx')