import Curso

class Unidade:

    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def getNome(self):
        return self.nome
    
    def setNome(self, valor):
        self.nome = valor

    def getCursos(self):
        return self.cursos
    
    def setCursos(self, valor):
        self.cursos = valor

    def adicionarCurso(self, valor):
        self.cursos.append(valor)

    def removerCurso(self, valor):
        self.cursos.remove(valor)