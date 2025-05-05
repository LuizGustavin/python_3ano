'''
doubro = float(input("digite um número para saber seu dobro: "))

def dobro(num):
    doubro = num * 2
    return doubro

print(dobro(doubro))
'''

'''
mosaico =  float(input("digite um numero para saber sua metade: "))

def metade(ladinho):
    metade = ladinho /2
    return metade

print(metade(mosaico))
'''

'''
numero = int(input("digite um numero para saber se é positivo ou negativo: "))

def eh_positivo(numero):
    if numero >0:
        print("seu numero é positivo")
    elif numero <0:
        print("seu numero é negativo")
    else :
        print("numero neutro (0)")
    return eh_positivo

print (eh_positivo(numero))
''' 

'''
def media_tres(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma / 3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado = media_tres(num1, num2, num3)
print("A média é:", resultado)
'''

'''
palavra1 = str(input("digite sua primeira palavra: "))
palavra2 = str(input("digite sua segunda palavra: "))

def comparar_palavra(palavra1,palavra2):
    if palavra1 == palavra2:
       return True
    elif palavra1 != palavra2:
        return False
    else :
        print("digite palavras validas")
    return(comparar_palavra(palavra1,palavra2))

if comparar_palavra(palavra1,palavra2):
    print("palavras iguais")
else :
    print("palavras diferentes")
'''

'''
idade = int(input("Digite sua idade: "))

def pode_votar(idade):
    if idade >= 16:
        return True
    else:
        return False

if pode_votar(idade):
    print("Você pode votar.")
else:
    print("Você não pode votar.")
'''

'''
numero = int(input("Digite um número inteiro positivo: "))
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


if numero < 0:
    print("Por favor, digite um número positivo.")
else:
    print(f"O fatorial de {numero} é {fatorial(numero)}.")
'''

def maior_lista(lista):
    maior = lista[]  
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

numeros = []

print("Digite 4 números:")

for i in range(4):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior_valor = maior_lista(numeros)
print(f"O maior número digitado é: {maior_valor}")
