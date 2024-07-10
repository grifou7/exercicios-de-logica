class Pessoa:

    def __init__(self, nome="", sexo="", cpf="", ano_nascimento=0, salario_bruto=0):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ano_nascimento = ano_nascimento
        self.idade = self.calcular_idade()
        self.salario_bruto = salario_bruto
        self.salario_liquido = self.calcular_salario_liquido()
        

    def calcular_irrf(self):
        salario = self.salario_bruto
        if salario >= 2259.21 and salario <= 2824.00:
         return salario - 564.80
        elif salario == 2826.65:
          return self.calcular_porcentagem(7.5)
        elif salario >= 2826.66 and salario <= 3751.05:
         return self.calcular_porcentagem(15.00)
        elif salario >= 3751.06 and salario <= 4664.68:
         return self.calcular_porcetagem(22.5)
        elif salario >= 4664.68:
         return self.calcular_porcentagem(27.5)
        else:
           return 0.0
        
    def calcular_salario_liquido(self):
       return self.salario_bruto - (self.calcular_inss() + self.calcular_irrf())
    
    def calcular_porcentagem(self, porcentagem):
       return (self.salario_bruto * porcentagem) / 100

    def calcular_inss(self):
        salario = self.salario_bruto
        if salario < 1412.01:
            return self.calcular_porcentagem(7.5)
        elif salario >= 1412.01 and salario <= 2666.68:
            return self.calcular_porcentagem(9.00)
        elif salario >= 2666.69 and salario <= 4000.03:
            return self.calcular_porcentagem(12.00)
        elif salario >= 4000.04:
            return self.calcular_porcentagem(14.00)

    def calcular_idade(self):
        return 2024 - self.ano_nascimento
    
    def informações(self):
        print(f"Nome:{self.nome}\nSxo:{self.sexo}\nCpf:{self.cpf}\nAno de nascimento:{self.ano_nascimento}\nIdade:{self.idade}\n{self.salario_bruto}\n{self.salario_liquido}")
    def calcular_salario_liquido(self):
       return self.salario_bruto - (self.calcular_inss() + self.calcular_irrf())
if __name__ == '__main__':
     Polako = Pessoa()
     Polako.nome = (input("Digite seu nome:"))
     Polako.cpf = (input("Digite seu cpf:"))
     Polako.salario_bruto = float(input("Digite o salario bruto:"))
     Polako.ano_nascimento = int(input("Digite o ano de nascimento"))
     Polako.sexo = (input("Digite seu sexo"))
     Polako.salario_liquido = Polako.calcular_salario_liquido()
     Polako.idade = Polako.calcular_idade()
     Polako.informações()
