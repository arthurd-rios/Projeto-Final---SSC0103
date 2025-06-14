from Unidade import Unidade
from Curso import Curso
from Disciplina import Disciplina

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from itertools import chain
from random import randint
from time import sleep
from unicodedata import normalize, category

def padronizarTexto(texto):

    if texto is None:
        return ""
    
    texto = texto.strip().lower()

    texto = normalize('NFD', texto)
    texto = ''.join(c for c in texto if category(c) != 'Mn')

    return texto

def Menu(unidades):

    while True:

        print()
        print()
        print()
        print()

        print("1 - Cursos por unidade")
        print("2 - Dados de um determinado curso")
        print("3 - Dados de todos os cursos")
        print("4 - Dados de uma determinada disciplina")
        print("5 - Disciplinas de uma unidade")
        print("6 - Dados de um curso aleatório")
        print("7 - Fechar programa")
        print()

        try:

            opcao = int(input("Selecione uma opção: "))
            print()

            if opcao == 1: # Funcionalidade 1

                for unidade in unidades:

                    unidade.imprimirCursos()

            elif opcao == 2: # Funcionalidade 2

                cursoencontrado = []

                nomecurso = input("Digite o nome do curso: ")
                print()

                for unidade in unidades:

                    for curso in unidade.getCursos():

                        if (padronizarTexto(nomecurso) == padronizarTexto(curso.getNome())):
                            cursoencontrado.append(curso)

                if len(cursoencontrado) == 0:

                    print(f"Curso {nomecurso} não encontrado")
                    print()

                else:
                    
                    print(f"{len(cursoencontrado)} curso(s) encontrado(s)")
                    print()
                    
                    for curso in cursoencontrado:
                        curso.imprimirDadosCurso()

            elif opcao == 3: # Funcionalidade 3

                for unidade in unidades:
                    
                    for curso in unidade.getCursos():
                        curso.imprimirDadosCurso()

            elif opcao == 4: # Funcionalidade 4

                disciplinaencontrada = []
                cursospresente = []

                codigodisciplina = input("Digite o código da disciplina: ")
                print()

                for unidade in unidades:

                    for curso in unidade.getCursos():

                        for disciplina in chain(curso.getObrigatorias(), curso.getOptativasLivres(), curso.getOptativasEletivas()):
                            
                            if(padronizarTexto(disciplina.codigo) == padronizarTexto(codigodisciplina)):

                                disciplinaencontrada.append(disciplina)
                                cursospresente.append(curso)

                                break

                if len(cursospresente) == 0:

                    print(f"Disciplina {codigodisciplina} não encontrada")
                    print()

                else:

                    disciplinaencontrada[0].imprimirDadosDisciplina()

                    print(f"Cursos em que {codigodisciplina} está presente: ")
                    print()

                    for curso in cursospresente:
                        print(curso.getNome())
                
                    print()


            elif opcao == 5: # Funcionalidade 5

                disciplinas = []

                for i, unidade in enumerate(unidades):

                    print(f"{i + 1} - {unidade.getNome()}")
                    print()

                while True:

                    try:

                        j = int(input("Selecione o número da unidade desejada: "))
                        print()

                        if j > 0 and j < len(unidades):
                            break
                            
                        else:

                            print("Número inválido")
                            print()

                    except ValueError:
                        print("Entrada inválida")
                        print()

                for curso in unidades[j - 1].getCursos():

                    for disciplina in chain(curso.getObrigatorias(), curso.getOptativasLivres(), curso.getOptativasEletivas()):
                        
                        if disciplina not in disciplinas:
                            disciplinas.append(disciplina)

                for disciplina in disciplinas:
                    disciplina.imprimirDadosDisciplina()

            elif opcao == 6: # Funcionalidade 6

                randomuni = randint(0, len(unidades) - 1)
                
                cursos = unidades[randomuni].getCursos()

                randomcurso = randint(0, len(cursos) - 1)

                cursos[randomcurso].imprimirDadosCurso()

            elif opcao == 7: # Fechar Programa
                break

            else:
                print("Opção Inválida")
                print()
    
        except ValueError:
            print("Entrada inválida")
            print()


while True:

    try:
        uninum = int(input("Digite o número de unidades que serão lidas (Máximo = 47): "))
        print()

        if 0 < uninum <= 47:
            break

        else:
            print("Entrada inválida")
            print()

    except ValueError:
        print("Entrada inválida")
        print()

unidades = []

nav = webdriver.Chrome()
wait = WebDriverWait(nav, 20)

nav.get("https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275")

for i in range (uninum):

    # Seleciona a unidade

    wait.until(lambda driver: len(Select(driver.find_element(By.ID, "comboUnidade")).options) > 1)

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

        sleep(1)

        htmlerro = nav.page_source
        souperro = BeautifulSoup(htmlerro, 'html.parser')

        erro = souperro.find('div', class_="ui-dialog-buttonset")

        if erro:
            
            curso = Curso(nomecurso, nomeunidade, " -- ", " -- ", " -- ")
            
            unidades[i].adicionarCurso(curso)

            botao = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.ui-dialog-buttonset button")))

            botao.click()

            continue

        # Avança para a grade curricular do curso

        select = wait.until(expected_conditions.element_to_be_clickable((By.ID, "step4-tab")))
        select.click()

        # Coleta e armazena dados do curso

        sleep(1)

        try:

            wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div#gradeCurricular table")))

        except TimeoutException:
            pass

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

Menu(unidades)