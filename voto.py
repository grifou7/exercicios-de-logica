nome.append input("Digite o seu nome completo: ")
idade = float(input("Digite sua idade: "))

if idade > 17 and idade < 71:
    print("Obrigaório ")
elif idade < 16:
    print("não vota ")
else:
    print("facultativo ")

