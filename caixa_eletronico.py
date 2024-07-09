import os 
nome = []
saldo = []
deposito = 0
saque = 0
quant_saques = 0
quant_depósitos = 0
pong = 99

def menu_completo():
  global pong
  global saque
  global saldo
  global quant_saques
  global quant_depósitos
  while pong != 0:
   pong = float((input(" \n" " Digite 1 para o extrato \n Digite 2 para o saque \n Digite 3 para depositar \n Digite 0 para sair \n" " ")))
   if pong == 1:
    print(f"Nome:{nome} || Saques:{quant_saques} || Depósitos:{quant_depósitos} || Saldo:{round(saldo,2)}")
   if pong == 2:
    sacar()
   if pong == 3:
    depositar()

def sacar ():
  global saque
  global saldo
  global quant_saques
  global quant_depósitos
  saque = float(input("Digite um valor para sacar: "))
  if saque > saldo:
    os.system("cls")
    print("saldo indisponivel")
  elif saque <= saldo:
    quant_saques = quant_saques + 1
    saldo = saldo - saque
    os.system("cls")
    print("saldo sacado com sucesso, saldo atual", round(saldo,2))
 
def depositar():
 global saque
 global saldo
 global quant_saques
 global quant_depósitos
 deposito = float(input("Digite um valor para depositar"))
 saldo = saldo + deposito
 quant_depósitos = quant_depósitos + 1
 os.system("cls")
 print("O seu novo saldo é ", (round(saldo,2)))
    
nome = (input("Digite seu nome:"))
saldo = float((input("Digite o valor inicial:")))
menu_completo()