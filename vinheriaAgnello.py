from datetime import datetime, date, timedelta

#Classe que representa o cadastro do cliente
class Cliente:
    def __init__(self, nome, cpf, endereco, enderecoEntrega):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.enderecoEntrega = enderecoEntrega




# Definição da quantidade de vinhos
class QuantidadeEspecifica:
    def __init__(self, numero, tipo, quantidade, quantidadeTipo):

        
        self.numero = numero

        #Vinho individual, meia duzia ou uma duzia
        self.tipo = tipo

        #Quantidade: a quantidade do tipo que for especificado, por exemplo: 6 vinhos individuais;
        #6 caixas de meia duzia
        #6 caixas de 1 duzia
        self.quantidade = quantidade

        self.quantidadeTipo = quantidadeTipo
        #Quantidade do tipo especificado 


        
        """
            1 / unitario / 1
            6 / meia-duzia/ 1
            12 / caixa / 1
        """
#Definição de uma class que apresentará os itens de saída, como vinhos individuais
class Produto:
    def __init__(self, numero, nome, quantidade, valor):
        self.numero = numero
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
#Classe que apresentará as informações sobre o frete
class Informacaofrete:
    def __init__(self, quantidadeGarrafa, valorGarrafa, porcentagemTotalPedido, valorPedido, totalFrete, data):
        self.quantidadeGarrafa = quantidadeGarrafa
        self.valorGarrafa = valorGarrafa
        self.porcentagemTotalPedido = porcentagemTotalPedido
        self.valorPedido = valorPedido
        self.totalFrete = totalFrete
        self.data = data
#Classe que apresentará as informações sobre as opções de data
class Data:
     def __init__(self, numero, opcao):
         self.numero = numero
         self.opcao = opcao
    

#Função que irá cadastrar o cliente, fazendo relação com a class de cliente feita
def cadastrarCliente():
    nome = input('Informe o  nome: ')
    cpf = input('Infome o cpf: ')
    endereco = input('Informe o endereço de onde está pedindo: ')
    enderecoEntrega = input('Informe o endereço de entrega: ')
    cliente = Cliente(nome, cpf, endereco, enderecoEntrega)
    return cliente
# Uma função que apresenta o cliente
def apresentaCliente(cliente):
    print(f"O cliente {cliente.nome}, \n cpf: {cliente.cpf}, \n endereço do pedido: {cliente.endereco}, \n endereço de entrega: {cliente.enderecoEntrega} "
          
          )

# função que cria lista de Vinhos
def criarListaDeVinho():
    vinho1 = Produto(1, 'Vinho Tinto', 200, 110.50)
    vinho2 = Produto(2, 'Vinho Branco', 200, 165.25)
    vinho3 = Produto(3, 'Vinho Rosé', 200, 133.33)
    vinho4 = Produto(4, 'Malbec', 200, 188.88)
    listaVinho = [
        vinho1,
        vinho2,
        vinho3,
        vinho4
    ]
    return listaVinho

# função que irá criar lista de quantidade
def criarListadeQuantidade():
    unitario = QuantidadeEspecifica(1, 'unitário', 0, 1)
    meiaDuzia = QuantidadeEspecifica(2, 'meia dúzia', 0, 6)
    caixa = QuantidadeEspecifica(3, 'caixa', 0, 12)
    listaQuantidade = [
        unitario,
        meiaDuzia,
        caixa

    ]
    return listaQuantidade

# Função que irá apresentar lista de quantidade
def apresentarListaQuantidade(lista):
    print('\n OPÇÕES: ')
    for item in lista:
        print(f"\n {item.numero} - {item.tipo}, {item.quantidadeTipo} por unidade")

# função onde será possível informar a opção, junto com a quantidade desejada do produto
def pedirQuantidadeEspecifica():
    listaQuantidade = criarListadeQuantidade()
    apresentarListaQuantidade(listaQuantidade)
   
    opcao = float(input('\n Informe a opção Desejada: '))
    quantidadeEscolhida = float(input('Qual a quantidade que você deseja desta opção: '))

    quantidade = 0

    for item in listaQuantidade:
        if(item.numero == opcao):
            if(item.tipo == 'unitário'):
                quantidade = item.quantidadeTipo * quantidadeEscolhida
            elif(item.tipo == 'caixa'):
                quantidade = item.quantidadeTipo * quantidadeEscolhida    
            elif(item.tipo == 'meia dúzia'):
                quantidade = item.quantidadeTipo * quantidadeEscolhida 
    

    return quantidade   
        
    
#Apresentando a lista de vinhos criadas
def apresentaListaDeVinho(listaVinho):
    print('LISTA DE VINHOS: ')
    for lista in listaVinho:
        print(f"{lista.numero} - {lista.nome}, {lista.quantidade} quantidades, R$ {lista.valor}")
    return lista
# Realiza o pedido do cliente, perguntando o item que ele deseja, a quantidade. Assim, também, o controle de estoque é feito
def realizarPedidoCliente(lista, listaCompras):
    itemLista = input('Selecione o item da lista que você gostaria: ')
    
    for item in lista:
        if(float(item.numero) == float(itemLista)):
            quantidadeItemLista = pedirQuantidadeEspecifica()
            if(item.quantidade >= quantidadeItemLista):
                item.quantidade -= quantidadeItemLista
                produto = Produto(0, item.nome, quantidadeItemLista, item.valor)
                listaCompras = somaQuantidadeOuAdicionaItemLista(produto, listaCompras)
            else:
                print('não tem esta quantidade disponível')
                print('LISTA ATUALIZADA ==>')
                apresentaListaDeVinho(lista)

            compraFinalizada = float(input('Deseje finalizar a compra? 1 para sim, 2 para não: '))
            
            if(compraFinalizada == 1):
                print('Pedido Finalizado')
            elif(compraFinalizada == 2):
               apresentaListaDeVinho(lista)
               realizarPedidoCliente(lista, listaCompras)
                
                
    return listaCompras
# Realiza a soma dos produtos escolhidos
def somaQuantidadeOuAdicionaItemLista(produto, listaCompra):
    if(len(listaCompras) > 0):
        for item in listaCompra:
            if(item.nome == produto.nome):
                item.quantidade += produto.quantidade
            else:
                listaCompra.append(produto)    
    else:
        listaCompra.append(produto)
    return listaCompra    

# Exibe os produtos escolhidos pelo cliente 
def exibirLista(carrinhoPedido):
    for item in carrinhoPedido:
        print('Nome: {}, Quantidade: {}, Valor: {}'
              .format(item.nome, item.quantidade, item.valor))

# Calcula o frete do pedido do cliente
def calcularPedidoComFrete(carrinhoPedido):
    valorTotal = 0
    quantidadeGarrafa = 0
    for item in carrinhoPedido:
         valorTotal += (item.quantidade * item.valor)
         quantidadeGarrafa += item.quantidade
    totalFrete = valorTotal * 0.1
    valorPedido = valorTotal + totalFrete + (quantidadeGarrafa * 10) + 10
    objData = escolherData()
    informacaoFrete = Informacaofrete(quantidadeGarrafa, 10, totalFrete, valorPedido, totalFrete, objData.opcao)
    return informacaoFrete

# Notifica o resultado final
def notificaResultado(resultadoComFrete):
    print('INFORMAÇÕES DO PEDIDO: ')
    print(f"O frete é R$ {resultadoComFrete.totalFrete}")
    print(f"O total é R$ {resultadoComFrete.valorPedido}")
    print(f"O numero de garrafas é {resultadoComFrete.quantidadeGarrafa}")
    print("A Data de entrega é {}".format(resultadoComFrete.data))
    

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

cliente = cadastrarCliente()
apresentaCliente(cliente)
input('Prossiga ')
lista = criarListaDeVinho()
apresentaListaDeVinho(lista)
listaCompras = []
carrinhoPedido = realizarPedidoCliente(lista,listaCompras)
exibirLista(carrinhoPedido)
resultadoComFrete = calcularPedidoComFrete(carrinhoPedido)
notificaResultado(resultadoComFrete)
input('')