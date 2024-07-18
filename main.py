class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome         #atributo público
        self._idade = idade      #atributo protegido
        self.__cpf = cpf         #atributo privado
    
    def imprimir_informacoes(self):
        print(f'Nome: {self.nome}, Idade: {self._idade}, CPF: {self.__cpf}')
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

class Estudante(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula  
