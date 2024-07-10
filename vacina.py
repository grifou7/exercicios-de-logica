nomes = []
data = []
vacina = []
id = []
lote = []
cpf = []
lista_nome = []
status = []
porrinha = 0
n = 0
def cadastro():
    global data
    global vacina
    global porrinha
    global id
    nome = (input("\nDigite o nome completo: "))
    nomes.append(nome)
    cpfs = (input("\nDigite seu cpf: "))
    cpf.append(cpfs)
    datas = (input("\nDigite a data de  nascimento: "))
    data.append(datas)
    vacinas = (input("\nDigite o nome da vacina: "))
    vacina.append(vacinas)
    porrinha += 1
    inicio()

def listar():
  global nomes
  global data
  global cpf
  global vacina
  id = 0
  status = []
  for i in range(porrinha):
    id += 1
    status
    print(f"__________________________\nID:{id}\nNomes:{nomes[i]}\nCpfs:{cpf[i]}\ndata:{data[i]}\nVacinas:{vacina[i]}")

def busca_cpf():
  global nomes
  global data
  global cpf
  global vacina
  global n
  global i 
  busca = (input("Digite um cpf para buscar"))
  if busca == 0:
   inicio()
  if busca != cpf[n]:
   print("cpf não registrado")
   busca_cpf() 
  while busca != cpf[n]:
   n += 1
  if busca  == cpf[n]:
   for i in range(1):
    print("o cpf é",busca)
    n = 0
   inicio()


def buscar():
  ping = 9
  while ping != 0:
    ping = (int(input("Selecione uma opção de busca")))
    if ping == 1:
      busca_cpf()
    if ping == 2:
      busca_nome()
    if ping == 3:
      busca_id()
    if ping == 4:
      busca_data()
    if ping == 5:
      busca_vacina()

def inicio():
 pong = 99
 while pong != 0:
  pong = (int(input("Aperte 1 para cadstrar|Aperte 2 para listar|Aperte 3 para buscar :")))
  if pong == 1:
   cadastro()
  if pong == 2:
   listar()
  if pong == 3:
    buscar()

inicio()