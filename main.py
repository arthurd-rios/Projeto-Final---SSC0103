from Unidade import Unidade
from Curso import Curso
from Disciplina import Disciplina

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup

import time

while True:
    try:
        uninum = int(input())
        break

    except ValueError:
        print("Entrada inválida")

unidades = []

nav = webdriver.Chrome()
wait = WebDriverWait(nav, 20)

nav.get("https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275")

for i in range (uninum):

    # Seleciona a unidade

    select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "comboUnidade")))
    select.send_keys(Keys.RETURN)
    select.send_keys(Keys.DOWN)
    select.send_keys(Keys.RETURN)

    # Cria e armazena uma unidade

    uselect = Select(select)

    nomeunidade = uselect.first_selected_option.text.strip()
    unidade = Unidade(nomeunidade)
    unidades.append(unidade)

    # Cria Select para conseguir todas as opções de curso

    wait.until(lambda driver: len(Select(driver.find_element(By.ID, "comboCurso")).options) > 1) # Função para aguardar o select ser populado

    select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "comboCurso")))
    cselect = Select(select)

    # Percorre todos os cursos da unidade

    for j in range (len(cselect.options) - 1):

        # Seleciona o curso

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "comboCurso")))
        select.send_keys(Keys.RETURN)
        select.send_keys(Keys.DOWN)
        select.send_keys(Keys.RETURN)

        cselect = Select(select)
        nomecurso = cselect.first_selected_option.text.strip()

        # Avança para o curso escolhido

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "enviar")))
        select.send_keys(Keys.RETURN)

        # Caso apareça o aviso de dados não encontrados



        # Avança para a grade curricular do curso

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "step4-tab")))
        select.click()

        # Coleta e armazena dados do curso

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div#gradeCurricular table")))

        html = nav.page_source

        soup = BeautifulSoup(html, "html.parser")

        durideal = soup.find('span', class_="duridlhab").get_text(strip=True)
        durmin= soup.find('span', class_="durminhab").get_text(strip=True)
        durmax = soup.find('span', class_="durmaxhab").get_text(strip=True)

        curso = Curso(nomecurso, nomeunidade, durideal, durmin, durmax)

        unidades[i].adicionarCurso(curso)

        # Coleta e armazena dados da disciplina

        tabelamaterias = soup.find('div', id="gradeCurricular").find_all('table')

        for tabela in tabelamaterias:

            tipotabela = tabela.find('tr').find('td').get_text(strip = True)

            materias = tabela.find_all('tr', style="height: 20px;")

            for materia in materias:

                dados = []

                infomateria = materia.find_all('td')

                for info in infomateria:

                    if(info.getText(strip = True) == ""):

                        dados.append("Não informado")

                    else:

                        dados.append(info.getText(strip = True))

                codigo = dados[0]
                nome = dados[1]
                crediaula = dados[2]
                creditrab = dados[3]
                ch = dados[4]
                che = dados[5]
                chp = dados[6]
                ativtpa = dados[7]

                disciplina = Disciplina(codigo, nome, crediaula, creditrab, ch, che, chp, ativtpa)

                if tipotabela == "Disciplinas Obrigatórias":
                    unidades[i].getCursos()[j].adicionarObrigatoria(disciplina)   

                elif tipotabela == "Disciplinas Optativas Livres":
                    unidades[i].getCursos()[j].adicionarOptativaLivre(disciplina)

                elif tipotabela == "Disciplinas Optativas Eletivas":
                    unidades[i].getCursos()[j].adicionarOptativaEletiva(disciplina)

                else:
                    print("Erro de alocação de disciplina")         

        # Retorna para a página de busca

        wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, "div.blockUI.blockOverlay")))

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "step1-tab")))
        select.click()

nav.quit()