from Unidade import Unidade
from Curso import Curso
from Disciplina import Disciplina

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
from itertools import chain
from random import randint

def Menu(unidades, uninum):

    while True:

        print("Selecione uma opção:")
        print()

        print("1 - Cursos por unidade")
        print("2 - Dados de um determinado curso")
        print("3 - Dados de todos os cursos")
        print("4 - Dados de uma determinada disciplina")
        print("5 - Disciplinas de uma unidade")
        print("6 - Dados de um curso aleatório")
        print("7 - Fechar programa")
        print()

        opcao = int(input())

        if opcao == 1: # Funcionalidade 1

            for unidade in unidades:

                unidade.imprimirCursos()

        elif opcao == 2: # Funcionalidade 2

            cursoencontrado = []

            nomecurso = input("Digite o nome do curso: ")

            for unidade in unidades:

                for curso in unidade.getCursos():

                    if (nomecurso == curso.getNome()):
                        cursoencontrado.append(curso)

            if len(cursoencontrado) == 0:

                print(f"Curso {nomecurso} não encontrado")
                print()

            else:
                cursoencontrado[0].imprimirDadosCurso()

        elif opcao == 3: # Funcionalidade 3

            for unidade in unidades:
                
                for curso in unidade.getCursos():
                    print(curso.imprimirDadosCurso())

        elif opcao == 4: # Funcionalidade 4

            disciplinaencontrada = []
            cursospresente = []

            codigodisciplina = input("Digite o código da disciplina: ")

            for unidade in unidades:

                for curso in unidade.getCursos():

                    for disciplina in chain(curso.getObrigatorias(), curso.getOptativasLivres(), curso.getOptativasEletivas()):
                        
                        if(disciplina.codigo == codigodisciplina):

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

                j = int(input("Selecione o número da unidade desejada: "))

                if j > 0 and j < uninum:
                    break
                    
                else:

                    print("Número inválido")
                    print()

            for curso in unidades[j - 1].getCursos():

                for disciplina in chain(curso.getObrigatorias(), curso.getOptativasLivres(), curso.getOptativasEletivas()):
                    
                    if disciplina not in disciplinas:
                        disciplinas.append(disciplina)

            for disciplina in disciplinas:
                disciplina.imprimirDadosDisciplina()

        elif opcao == 6: # Funcionalidade 6

            randomuni = randint(0, uninum - 1)
            
            cursos = unidades[randomuni].getCursos()

            randomcurso = randint(0, len(cursos) - 1)

            cursos[randomcurso].imprimirDadosCurso()

        elif opcao == 7: # Fechar Programa
            break

        else:
            print("Opção Inválida")
            print()


while True:
    try:
        uninum = int(input("Digite o número de unidades que serão lidas: "))
        break

    except ValueError:
        print("Entrada inválida")

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

Menu(unidades, uninum)