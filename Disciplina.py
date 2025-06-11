class Disciplina:

    def __init__(self, codigo, nome, crediaula, creditrab, ch, che, chp, ativtpa):
        
        self.codigo = codigo
        self.nome = nome
        self.crediaula = crediaula
        self.creditrab = creditrab
        self.ch = ch
        self.che = che
        self.chp = chp
        self.ativtpa = ativtpa

    def getCodigo(self):
        return self.codigo
    
    def setCodigo(self, valor):
        self.codigo = valor       

    def getNome(self):
        return self.nome
    
    def setNome(self, valor):
        self.nome = valor  

    def getCredAula(self):
        return self.crediaula
    
    def setCrediAula(self, valor):
        self.crediaula = valor  

    def getCrediTrab(self):
        return self.creditrab
    
    def setCrediTrab(self, valor):
        self.creditrab = valor  

    def getCargaHoraria(self):
        return self.ch
    
    def setCargaHoraria(self, valor):
        self.ch = valor  

    def getCargaHorariaEstag(self):
        return self.che
    
    def setCargaHorariaEstag(self, valor):
        self.che = valor  

    def getCargaHorariaPraticas(self):
        return self.chp
    
    def setCargaHorariaPraticas(self, valor):
        self.chp = valor  

    def getAtividadesTPA(self):
        return self.ativtpa
    
    def setAtividadesTPA(self, valor):
        self.ativtpa = valor   