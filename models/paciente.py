class Paciente:
    def __init__(self,id, cpf, nome, idade, celular, email):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def to_dict(self):
        return self.__dict__
        