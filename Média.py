nome = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Diigite a quarta nota: "))
média = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f"O aluno(a) {nome} ficou com uma média de {média}")
if média >= 7.0:
    print(f"O Aluno(a) {nome} foi aprovado ")
elif média <= 5.0:
    print("O aluno ficou de xereca")
else:
    print("O aluno ficou de recuperação")   