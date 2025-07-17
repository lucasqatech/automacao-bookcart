"""
Teste automatizado no site Book Cart
Objetivo:
- Pesquisar um livro específico

Site: https://bookcart.azurewebsites.net
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do navegador
navegador = webdriver.Firefox()
navegador.get("https://bookcart.azurewebsites.net")
navegador.maximize_window()
navegador.implicitly_wait(10)

try:
    livro = "Roomies"
    print(f"Buscando pelo livro: {livro}")
    
    campo_pesquisa = navegador.find_element(By.XPATH, "//input[@type='search']")
    campo_pesquisa.clear()
    campo_pesquisa.send_keys(livro)
    campo_pesquisa.send_keys(Keys.RETURN)
    
    WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//app-book-card//h4[contains(text(), '{livro}')]"))
    )
    print(f"Livro '{livro}' encontrado com sucesso.")

except Exception as erro:
    print(f"[ERRO] Ocorreu um problema na busca: {erro}")

finally:
    navegador.quit()
    print("Teste finalizado. Navegador fechado.")
