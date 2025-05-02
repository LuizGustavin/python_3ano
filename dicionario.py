# dicionario = {}
'''aluno = {
    "id":1,
    "nome":"jão gui",
    "idade": 17
}
print (aluno.values())
for chaves, valor in aluno.items():
    print("chave: ",chaves, "valor: ", valor )
'''

'''aluno = {
    "id":1,
    "nome":"jão gui",
    "idade": 17,
    "notas": []
}   

    {"id":2,
    "nome":"andré",
    "idade":16,
    "notas":[]
}


for i in range(3):
    aluno["notas"].append(float(input("informe suas notas: ")))

print(aluno1["nome"]) 
print (aluno1["notas"])
'''

'''
dicionario = {
    "12345678900":{
        "nome":"Luiz",
        "idade": 19,
        "cidade": "petrolina",
    },

    "11122233300":{
        "nome":"geraldo",
        "idade":20,
        "cidade":"juazeiro"

    }

}'''

'''
boletim = {}

qnts_pessoas = int(input("informe a quantidade de alunos que deseja cadastrar: "))
for i in range(qnts_pessoas):
    nome = input("nomes das pessoas:") 
    nota = float(input(f"qual a nota de {nome}: "))
    boletim[nome] = nota

print("<------------------------------------------------------------------------------------------------->")       

for nome,nota in boletim.items():
    print(f"o aluno {nome} tem nota igual a {nota}")

print("<------------------------------------------------------------------------------------------------->")       

buscador = str(input("Digite o nome do aluno que você deseja saber a nota: "))
if buscador in boletim:
    print(f"a nota do aluno{buscador} é : {boletim[buscador]} ")
else:
    print("nome informado não cadastrado")

print("<------------------------------------------------------------------------------------------------->")       

maior_nota = max(boletim.values())
menor_nota = min(boletim.values())
media = sum(boletim.values()) / len(boletim)

print("a maior nota é: ", maior_nota)
print("a menor nota é: ", menor_nota)
print("a média da turma é: ", media)
'''
catalogo = {}

qnts_filmes = int(input("informe a quantidade de filmes que deseja cadastrar: "))
for i in range(qnts_filmes):
    titulo = input("titulos dos filmes:") 
    ano = int(input("informe o ano de lançamento do filme: "))
    catalogo[titulo] = ano
   
print("<------------------------------------------------------------------------------------------------->")       

for filme, ano in catalogo.item():
    print(f"Filme:{filme} | ano:{ano}")

print("<------------------------------------------------------------------------------------------------->")       

buscador_filme = input("informe o titulo do filme que você procura: ")
if buscador_filme in catalogo:
    print(f"o ano do filme {buscador_filme} é: {catalogo[buscador_filme]}")
else:
    print("o titulo que você digitou não foi encontrado") 

print("<------------------------------------------------------------------------------------------------->")       


