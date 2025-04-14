class Funcionarios:
    def __init__(self, nome, cpf,  salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        
     # Getters
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_salario(self):
        return self.__salario
    
    # Setters
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def set_salario(self, salario):
        self.__salario = salario
        
    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"Salário: {self.__salario}")
        
        
class Gerente(Funcionarios):
    def __init__(self, nome, salario, cpf, setor):
        super().__init__(nome, salario, cpf)
        self.__setor = setor
       
    # Getter e Setter para bonus
    def get_bonus(self):
        return self.__bonus
    
    def set_bonus(self, bonus):
        self.__bonus = bonus
        
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Setor: {self.__setor}")
        print(f"Bonus: {self.__bonus}")
        print(f"Salário: R$ {self.__salario + self.__bonus}")
        print(f"Bônus: R$ {self.__bonus}")
        print(f"Salário Final: R$ {self.__salario + self.__bonus}")
        
        
class Operacional(Funcionarios):
    def __init__(self, nome, salario, cpf, setor):
        super().__init__(nome, salario, cpf)
        self.__setor = setor
        
        # Getter e Setter para turno
    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    def exibir_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Salário: R$ {self.get_salario():.2f}")
        print(f"Turno: {self.__turno}")
