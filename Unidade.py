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

    def imprimirCursos(self):

        print(f"Lista de cursos da unidade {self.nome}:")
        print()

        for i, curso in enumerate(self.cursos):

            print(f"{i+1} - {curso.getNome()}")

        print()