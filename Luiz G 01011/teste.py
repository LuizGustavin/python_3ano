estoque = {}

# Pergunta quantos produtos o usuário deseja cadastrar
itens = int(input("Quantos itens você quer cadastrar? "))

# Loop para cadastrar os produtos
for i in range(itens):
    nome_produto = input("Qual o nome do produto? ")
    quantidade_produto = int(input("E qual a quantidade? "))
    
    # Armazena o produto no dicionário
    estoque[nome_produto] = quantidade_produto

# Exibe todos os produtos cadastrados
print("Produtos cadastrados no estoque:")
for nome, quantidade in estoque.items():
    print(f"{nome} | {quantidade} unidades")

# Pergunta qual produto o usuário deseja buscar
busca = input("\nQual produto você está procurando? ")

# Verifica se o produto está no estoque
if busca in estoque:
    # Exibe a quantidade do produto encontrado
    print(f"O produto {busca} está no estoque com {estoque[busca]} unidades.")
else:
    print("O produto não está cadastrado.")
