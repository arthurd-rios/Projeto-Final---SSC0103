import Unidade

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions

import time

while True:
    try:
        uninum = int(input())
        break

    except ValueError:
        print("Entrada inválida")

nav = webdriver.Chrome()
wait = WebDriverWait(nav, 10)

nav.get("https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275")

for i in range (uninum):

    # Seleciona a unidade

    select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "comboUnidade")))
    select.send_keys(Keys.RETURN)
    select.send_keys(Keys.DOWN)
    select.send_keys(Keys.RETURN)

    # Cria e armazena uma unidade



    # Cria Select para conseguir todas as opções de curso

    wait.until(lambda driver: len(Select(driver.find_element(By.ID, "comboCurso")).options) >= 1) # Função para aguardar o select ser populado

    select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "comboCurso")))
    cselect = Select(select)

    # Percorre todos os cursos da unidade

    for j in range (len(cselect.options) - 1):

        # Seleciona o curso

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "comboCurso")))
        select.send_keys(Keys.RETURN)
        select.send_keys(Keys.DOWN)
        select.send_keys(Keys.RETURN)

        # Avança para o curso escolhido

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "enviar")))
        select.send_keys(Keys.RETURN)

        # Avança para a grade curricular do curso

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "step4-tab")))
        select.click()


        # Coleta e armazena as informações



        # Retorna para a página de busca

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "step1-tab")))
        select.click()

nav.quit()
