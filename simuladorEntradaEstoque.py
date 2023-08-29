from datetime import datetime, date, timedelta
#Classe que irá auxiliar no cadastro do Fornecedor
class Fornecedor:
    def __init__(self, nome, cnpj, endereco, enderecoEntrega):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.enderecoEntrega = enderecoEntrega

#Definição de uma class que apresentará os itens de entrada, como rolhas, garrafas etc...
class ItemEstoque:
    def __init__(self, numero, item, quantidade):
        self.numero = numero
        self.item = item
        self.quantidade = quantidade

#Classe que apresentará as informações sobre as opções de data
class Data:
     def __init__(self, numero, opcao):
         self.numero = numero
         self.opcao = opcao

def cadastrarfornecedor():
    nome = input('Informe o  nome: ')
    cnpj = input('Infome o cnpj: ')
    endereco = input('Informe o endereço de onde está pedindo: ')
    enderecoEntrega = input('Informe o endereço de entrega: ')
    fornecedor = Fornecedor(nome, cnpj, endereco, enderecoEntrega)
    return fornecedor
# Uma função que apresenta o fornecedor
def apresentafornecedor(fornecedor):
    print(f"O fornecedor {fornecedor.nome}, \n cnpj: {fornecedor.cnpj}, \n endereço do pedido: {fornecedor.endereco}, \n endereço de entrega: {fornecedor.enderecoEntrega} "
          
          )

#Função que cria lista de entrada
def criarListaDeEntrada():
    entradaRolhas = ItemEstoque(1, 'Rolhas', 0)
    entradaGarrafas = ItemEstoque(2, 'Garrafas', 0)
    entradaRotulos = ItemEstoque(3, 'Rótulos', 0)
    entradaCaixas = ItemEstoque(4, 'Caixas', 0)
    listaEntradaItens = [
        entradaRolhas,
        entradaGarrafas,
        entradaRotulos,
        entradaCaixas
    ]
    return listaEntradaItens

#Função que irá apresentar lista de entrada
def apresentaListaEntrada(lista):
    print("LISTA DE ENTRADA: ")
    for register in lista:
        print(f"{register.numero} - {register.item}")


#Função que cria lista de entrada
def criarListaDeEntrada():
    entradaRolhas = ItemEstoque(1, 'Rolhas', 0)
    entradaGarrafas = ItemEstoque(2, 'Garrafas', 0)
    entradaRotulos = ItemEstoque(3, 'Rótulos', 0)
    entradaCaixas = ItemEstoque(4, 'Caixas', 0)
    listaEntradaItens = [
        entradaRolhas,
        entradaGarrafas,
        entradaRotulos,
        entradaCaixas
    ]
    return listaEntradaItens

#Função que irá apresentar lista de entrada
def apresentaListaEntrada(lista):
    print("LISTA DE ENTRADA: ")
    for register in lista:
        print(f"{register.numero} - {register.item}")
# Função onde se dará a ação de escolher as opções de entrada
def escolherEntrada(listaEstoque):
    listaEntrada = criarListaDeEntrada()
    apresentaListaEntrada(listaEntrada)
    opcao = float(input('Selecione o item que você deseja que entre: '))
    for register in listaEntrada:
        if(register.numero == opcao):
            quantidade = float(input('Informe a quantidade que você deseja: '))
            itemEstoque = ItemEstoque(0, register.item, quantidade)
            listaEstoque = somaQuantidadeOuAdicionaItemLista(itemEstoque, listaEstoque)
    compraFinalizada = float(input('Deseje finalizar a compra? 1 para sim, 2 para não: '))    
    if(compraFinalizada == 1):
                print('Pedido Finalizado')
    elif(compraFinalizada == 2):
               escolherEntrada(listaEstoque)

    return listaEstoque

# Irá apresentar o estoque
def apresentaEstoque(listaEstoque):
     print('SEU PEDIDO: ')
     for item in  listaEstoque:
          if(item.quantidade > 0):
            print(" {}, cujo a quantidade é {}".format(item.item, item.quantidade))
            
        
def somaQuantidadeOuAdicionaItemLista(itemEstoque, listaAtualizada):
    if(len(listaAtualizada) > 0):
        for register in listaAtualizada:
            if(register.item == itemEstoque.item):
                register.quantidade += itemEstoque.quantidade
            else:
                listaAtualizada.append(itemEstoque)    
    else:
        listaAtualizada.append(itemEstoque)
    return listaAtualizada

# Cria a lista de opções de data que se poderá escolher 
def criarListaData():
    today  = date.today()
    data3dias = today + timedelta(days=3)
    data7dias = today + timedelta(days=7)
    data10dias = today + timedelta(days=10)

    dataDiferenca3DiasPosterior = Data(1, data3dias)
    dataDiferenca7DiasPosterior = Data(2, data7dias)
    dataDiferenca10DiasPosterior = Data(3, data10dias)
    listaData = [
        dataDiferenca3DiasPosterior,
        dataDiferenca7DiasPosterior,
        dataDiferenca10DiasPosterior
    ]
    return listaData
# Apresentando a lista feita pelo metódo acima
def apresentaData(listaData):
    print('\n DATAS DE ENTREGA: ')
    for item in listaData:
         print(f"\n {item.numero} - {item.opcao}")
# Método que permite a escolha das datas apresentadas
def escolherData():
    listaData = criarListaData()
    apresentaData(listaData)
    
    escolherOpcao = float(input("escolha a opção de data que você deseja que seja entregue: "))
    data = ''
    for item in listaData:
        if(escolherOpcao == item.numero):
            data = item

    return data
fornecedor = cadastrarfornecedor()
apresentafornecedor(fornecedor)
listaEstoque = []
listaAtualizada = escolherEntrada(listaEstoque)
dataEscolhida = escolherData()
apresentaEstoque(listaAtualizada)

input('voce escolheu a data: {} '.format(dataEscolhida.opcao))
input('')
