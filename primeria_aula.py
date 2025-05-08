'''class Cliente:
    def __init__(self,nome,fone):
        
        self.nome = nome
        self.telefone = fone 

    def informacoes(self):
        print("informaçoes do cliente")
        print(f"nome: {self.nome}") 
        print(f"telefone {self.telefone}")


c1 = Cliente( "jãozin","87988231248")
c2 = Cliente( "lester","87988752931")

c1.informacoes()
c2.informacoes()
'''


'''------------------------------------------------------------------------------------------------------------------------'''



class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano
        self.estado = False

    def desligar(self):
        self.estado = False
        print(f"o carro {self.modelo} está desligado")

    def ligado(self):
        self.estado = True
        print(f"o carro {self.modelo} está ligado")

       
    
    def informacoes(self):
        aux = "ligado" if self.estado else "desligado"
        print(f"marca do carro: {self.marca}")
        print(f"o modelo do carro: {self.modelo}")
        print(f"o ano: {self.ano}")
        print(f"estado: {aux}")

carros = []

while True:
    print("\n         menu\n")
    print("1. Resgistre um novo carro ")
    print("2. Ligar carro")
    print("3. Desligar carro")
    print("4. Visulizar informações dos carros")
    print("5. sair")
    
    escolha = int(input("escolha uma das opções 1 à 5: "))
    if escolha == 1:
        marca = str(input("digite a marca do carro: "))
        modelo = str(input("digite o modelo do carro: "))
        ano = int(input("digite o ano do carro: "))
        carro = Carro(marca, modelo, ano)
        carros.append(carro)
        print(f"Carro {modelo} cadastrado com sucesso!")
    
        print("-"*100)

    elif escolha == 2: 
        modelo = str(input("qual o modelo você quer ligar: "))
        for i in carros:
            if i.modelo  == modelo:
                i.ligado()
                break
        else:
            print("modelo não encontrado")

        print("-"*100)

    elif escolha == 3:
        modelo = input("qual o modelo você deseja desligar: ")
        for i in carros:
            if i.modelo == modelo:
                i.desligar()
                break
        else:
            print("modelo não encontrado")
    
        print("-"*100)

    elif escolha == 4:
        print("LISTA DE CARROS QUE ESTÃO DISPONÍVEIS")
        for c in carros:
            c.informacoes()
    elif escolha == 5:
        print("Saindo....")
        break
    else:
      print("escolha uma opção válida")
