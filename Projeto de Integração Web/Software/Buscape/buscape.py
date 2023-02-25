import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


def buscape (nav, produto, termos_banidos, preco_minimo, preco_maximo):
    produto =  produto.lower()
    termos_banidos = termos_banidos.lower()
    list_termos_ban = termos_banidos.split(" ")
    list_termos_produtos = produto.split(" ")
    preco_minimo = float(preco_minimo)
    preco_maximo = float(preco_maximo)
    time.sleep(5)
    nav.get('https://www.buscape.com.br/?og=19220&og=19220&gclid=EAIaIQobChMIq6Txtr3O9gIVTgmRCh1rtAs_EAAYASAAEgLHHfD_BwE')
    nav.find_element(By.CLASS_NAME, 'AutoCompleteStyle_input__FInnF').send_keys(produto)
    nav.find_element(By.CLASS_NAME, 'AutoCompleteStyle_input__FInnF').send_keys(Keys.ENTER)
    time.sleep(5)
    
    lista_resultado = []
    resultado = nav.find_elements(By.CLASS_NAME, ('Cell_Content__fT5st'))
    for resultad in resultado:
        name = resultad.get_attribute('title')
        name = name.lower()
        # Testa Termos Banidos
        tem_termos_banidos = False
        for item in list_termos_ban:
            if item in name:
                tem_termos_banidos = True
            # Testa a Existência de Todos os Termos
        tem_todos_os_termos = True
        for item in list_termos_produtos:
            if item not in name:
                tem_todos_os_termos = False
        #print(tem_todos_os_termos, tem_termos_banidos)
        try:
            if tem_termos_banidos == False and tem_todos_os_termos == True:
                preco = resultad.find_element(By.CLASS_NAME, 'CellPrice_MainValue__3s0iP').text
                preco = preco.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')
                preco = float(preco)
                if preco_minimo <= preco <= preco_maximo:
                    link1 = resultad.get_attribute('href')
                    lista_resultado.append((name, preco, link1))
        except:
            continue
    return lista_resultado

roda_bot = buscape()
