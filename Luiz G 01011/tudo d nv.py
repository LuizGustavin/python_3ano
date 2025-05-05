'''
lista_numeros = []
for i in range (5):
    lista_numeros.append(int(input("informe um número inteiro: ")))
    
if lista_numeros == sorted(lista_numeros):
    print("SIM")
else:
    print("NÃO")
'''



'''
numeros = []
for i in range(5):
    numeros.append(int(input("informe um número: ")))
numeros.reverse()
print("lista invertida: ", numeros)
numeros.reverse()
numeros.insert(1,35)
print("a lista pós modificacão: ", numeros)

if 7 in numeros:
    while 7 in numeros:
        numeros.remove(7)
    print("lista após remocão do número 7: ", numeros)
    
else:
     print("não existe número 7 na lista")

if 45 in numeros:
    print(f"posicão do numero 45: {numeros.index(45)}")
else:
    print("não existe número 45 na lista")       
'''



'''
estoque={}

itens = int(input("quantos itens você quer cadastrar: "))
for i in range(itens):
    nome_produto = str(input("qual o nome do produto: "))
    quantidade_produto = int(input("E qual a quantidade: "))
    estoque[nome_produto] = quantidade_produto   
print("produtos cadastrados: ")

for nome, quantidade in estoque.items():
    print(f"numero de produtos cadastrados:{nome} | {quantidade} unidades ")
busca = str(input("qual produto você esta procurando?: "))
if busca in estoque:
    print(f"o {busca} esta no estoque com {estoque} unidades")
else:
    print("o produto não esta cadastrado")
'''

def progressao_aritimeditca (termo):
    
    primeiro_termo = float(input("digit"))

