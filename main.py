import selenium
from selenium.webdriver.common.by import By
import Unidade

nav = selenium.webdrive.Chrome()

nav.get("https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275")

selectoptions = nav.find_element(By.ID, "comboUnidade")
selectoptions.click()

# seleciona a proxima unidade da ordem (tlvz tenha que pular o primeiro)
# find no id de "curso" e depois clica
# seleciona o proximo curso da ordem (tlvz tenha que pular o primeiro)
# find no id do botão buscar e depois clica

# find no id do botão Grade Curricular e depois clica 
# baixa html e armazena tudo nas classes

# find no id do botão superior de buscar e depois clica
# find no id de limpar e clica em seguida