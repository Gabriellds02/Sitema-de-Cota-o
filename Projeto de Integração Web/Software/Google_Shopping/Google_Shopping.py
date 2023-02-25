import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

# Função GOOGLE SHOPPING
def busca_google_shopping (nav, produto, termos_banidos, preco_minimo, preco_maximo):
    produto =  produto.lower()
    termos_banidos = termos_banidos.lower()
    list_termos_ban = termos_banidos.split(" ")
    list_termos_produtos = produto.split(" ")

    nav.get('https://www.google.com/')
    nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(produto)
    nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    elemento = nav.find_elements(By.CLASS_NAME, 'hdtb-mitem')
    for item in elemento:
        if "Shopping" in item.text:
            item.click()
            break
    

    lista_resultados = []
    resultado = nav.find_elements(By.CLASS_NAME, 'KZmu8e')
    for result in resultado:
    ##### Name #########
        name = result.find_element(By.CLASS_NAME, 'sh-np__product-title').text
        name = name.lower()

        tem_termos_banidos = False
        for termos in list_termos_ban:
            if termos in name:
                tem_termos_banidos = True
        
        tem_todos_os_produtos = True
        for termos in list_termos_produtos:
            if termos not in name:
                tem_todos_os_produtos = False

        if not tem_termos_banidos and tem_todos_os_produtos: # mesma coisa -> if not tem_termos_banidos and tem_todos_os_produtos: 
            try:
            ##### Preço #######
                preco = result.find_element(By.CSS_SELECTOR,'b.translate-content').text
                time.sleep(0.1)
                preco = preco.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
                preco = float(preco)

                preco_minimo = float(preco_minimo)
                preco_maximo = float(preco_maximo)
                if preco_minimo <= preco <= preco_maximo:
            ##### Link #########
                    name_link = result.find_element(By.CLASS_NAME, 'E5ocAb').text
                    link = result.find_element(By.CLASS_NAME, 'SirUVb')
                    link_result = link.find_element(By.XPATH, '..')
                    link_select = link_result.get_attribute('href')
                    #print(f'Nome:{name}, Preço: {preco}, Link: {link_result}')
                    lista_resultados.append((name, preco, link_select))
            except:
                continue
    return lista_resultados
