class cachorro:

    def __init__(self, raça, cor, nome, sexo, peso, altura, data_nascimento, quantidade_comida_porcao):
        self.raça = raça
        self.cor = cor
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.data_nascimento = data_nascimento
        self.quantidade_comida_porcao = quantidade_comida_porcao
        self.comida = 1000

    def comer(self):
       self.comida -= self.quantidade_comida_porcao
       print(f"O cachorro {self.nome} ainda possui {self.comida} gramas.")

    def latir(self):
       print(f"O cachorro {self.nome} esta latindo")

    def informações(self):
       print(f"O cachorro {self.nome} tem {self.peso} Kgs e {self.altura} centimetros, sua raça é {self.raça} sua cor é {self.cor}, ele nasceu em {self.data_nascimento} e tem {self.comida} de ração")


if __name__ == '__main__':
 meu_primeiro_cachorro  = cachorro("gay", "Amazul", "Cucabeludo", "neutro", 55555.3000, 32.5, "01/01/2001", 700)
 print(meu_primeiro_cachorro.nome)
 segundo_cachorro = cachorro("Polako", "Gayazonu", "João", "Feminino", 34.500, 23.9, "1198/06/09", 200)
meu_primeiro_cachorro.latir()
segundo_cachorro.comer()
segundo_cachorro.informações()