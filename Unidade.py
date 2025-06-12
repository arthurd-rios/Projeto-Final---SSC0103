import Curso

class Unidade:

    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def getUnidade(self):
        return self.unidade
    
    def setUnidade(self, valor):
        self.unidade = valor

    def getCursos(self):
        return self.cursos
    
    def setCursos(self, valor):
        self.cursos = valor

    def adicionarCurso(self, valor):
        self.cursos.append(valor)

    def removerCurso(self, valor):
        self.cursos.remove(valor)