nome = input("Digite o nome do aluno: ")
notas = []


def ler_nota():
 notas.append(float(input("Digite uma nota")))

def calcular_média():
 somatorio = sum(notas)
 print(somatorio)
 média = somatorio / (len(notas))
 print(round(média,2))
 
ler_nota()
ler_nota()
ler_nota()
ler_nota()
calcular_média()
print(max(notas))
print(min(notas))



 



print(notas)
print(len(notas))

notas.append(7.5)
notas.append(8.5)
notas.append(3.5)

print(notas)

notas.pop
print(notas)
