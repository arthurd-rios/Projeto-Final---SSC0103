import Disciplina

class Curso:

    def __init__(self, nome, unidade, duracaoideal, duracaomin, duracaomax):

        self.nome = nome
        self.unidade = unidade
        self.duracaoideal = duracaoideal
        self.duracaomin = duracaomin
        self.duracaomax = duracaomax
        self.obrigatorias = []
        self.optlivres = []
        self.opteletivas = []

    def getNome(self):
        return self.nome
    
    def setNome(self, valor):
        self.nome = valor  

    def getUnidade(self):
        return self.unidade
    
    def setUnidade(self, valor):
        self.unidade = valor  

    def getDuracaoIdeal(self):
        return self.duracaoideal
    
    def setDuracaoIdeal(self, valor):
        self.duracaoideal = valor  

    def getDuracaoMinima(self):
        return self.duracaomin
    
    def setDuracaoMinima(self, valor):
        self.duracaomin = valor  

    def getDuracaoMaxima(self):
        return self.duracaomax
    
    def setDuracaoMaxima(self, valor):
        self.duracaomax = valor  

    def getObrigatorias(self):
        return self.obrigatorias
    
    def setObrigatorias(self, valor):
        self.obrigatorias = valor  

    def getOptativasLivres(self):
        return self.optlivres
    
    def setOptativasLivres(self, valor):
        self.optlivres = valor  

    def getOptativasEletivas(self):
        return self.opteletivas
    
    def setOptativasEletivas(self, valor):
        self.opteletivas = valor  

    def adicionarObrigatoria(self, valor):
        self.obrigatorias.append(valor)

    def removerObrigatoria(self, valor):
        self.obrigatorias.remove(valor)

    def adicionarOptativaLivre(self, valor):
        self.optlivres.append(valor)

    def removerOptativaLivre(self, valor):
        self.optlivres.remove(valor)

    def adicionarOptativaEletiva(self, valor):
        self.opteletivas.append(valor)

    def removerOptativaEletiva(self, valor):
        self.opteletivas.remove(valor)