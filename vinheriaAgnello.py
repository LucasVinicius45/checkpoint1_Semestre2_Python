#Classe que representa o cadastro do cliente
class Cliente:
    def __init__(self, nome, cpf, endereco, enderecoEntrega):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.enderecoEntrega = enderecoEntrega

#Definição de uma class que apresentará os itens de entrada, como rolhas, garrafas etc...
class ListaItensEstoque:
    def __init__(self, rolhas, garrafas, rotulos, caixas):
        self.rolhas = rolhas
        self.garrafas = garrafas
        self.rotulos = rotulos
        self.caixas = caixas


# Definição da quantidade de vinhos
class QuantidadeEspecifica:
    def __init__(self, quantidade, tipo, quantidadeTipo):

        #Quantidade: a quantidade do tipo que for especificado, por exemplo: 6 vinhos individuais;
        #6 caixas de meia duzia
        #6 caixas de 1 duzia
        self.quantidade = quantidade

        #Vinho individual, meia duzia ou uma duzia
        self.tipo = tipo

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
    
# Definicão do pedido
class PedidosCliente:
    def __init__(self, cliente, especificaPedido, quantidade: QuantidadeEspecifica, codigoIdentificacao, dataEntrega):
        self.cliente = cliente
        self.especificaPedido = especificaPedido
        self.quantidade = quantidade
        self.codigoIdentificacao = codigoIdentificacao
        self.dataEntrega = dataEntrega

class Informacaofrete:
    def __init__(self, quantidadeGarrafa, valorGarrafa, porcentagemTotalPedido, valorPedido, totalFrete):
        self.quantidadeGarrafa = quantidadeGarrafa
        self.valorGarrafa = valorGarrafa
        self.porcentagemTotalPedido = porcentagemTotalPedido
        self.valorPedido = valorPedido
        self.totalFrete = totalFrete
    

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
    print(f"O cliente {cliente.nome}, \n cpf: {cliente.cpf}, \n endereço do pedido: {cliente.endereco}, \n endereco de entrega: {cliente.enderecoEntrega} "
          
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

def pedirQuantidadeEspecifica():
    tipoQuantidade = input('Qual tipo de unidade você deseja? unitaria, caixa(12) ou meia duzia(6)')
    quantidadeIPorTipo = float(input('Informe a quantidade ({}): '.format(tipoQuantidade)))

    quantidade = 0

    if(tipoQuantidade == 'unitaria'):
        quantidade = quantidadeIPorTipo
    elif(tipoQuantidade == 'caixa'):
        quantidade = quantidadeIPorTipo * 12    
    elif(tipoQuantidade == 'meia duzia'):
        quantidade = quantidadeIPorTipo * 6 

    return quantidade   
        
    
#Apresentando a lista de vinhos criadas
def apresentaListaDeVinho(listaVinho):
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
                print('não tem esta quatidade disponível')
                print('LISTA ATUALIZADA ==>')
                apresentaListaDeVinho(lista)

            compraFinalizada = float(input('Deseje finalizar a compra? 1 para sim, 2 para não: '))
            
            if(compraFinalizada == 1):
                print('Compra Finalizada')
            elif(compraFinalizada == 2):
               realizarPedidoCliente(lista, listaCompras)
                
                
    return listaCompras

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

        
def exibirLista(carrinhoPedido):
    for item in carrinhoPedido:
        print('Nome: {}, Quantidade: {}, Valor: {}'
              .format(item.nome, item.quantidade, item.valor))

def calcularPedidoComFrete(carrinhoPedido):
    valorTotal = 0
    quantidadeGarrafa = 0
    for item in carrinhoPedido:
         valorTotal += (item.quantidade * item.valor)
         quantidadeGarrafa += item.quantidade
    totalFrete = valorTotal * 0.1
    valorPedido = valorTotal + totalFrete + (quantidadeGarrafa * 10) + 10
    informacaoFrete = Informacaofrete(quantidadeGarrafa, 10, totalFrete, valorPedido, totalFrete)
    return informacaoFrete
    
##cliente = cadastrarCliente()
##apresentaCliente(cliente)
lista = criarListaDeVinho()
apresentaListaDeVinho(lista)
listaCompras = []
carrinhoPedido = realizarPedidoCliente(lista,listaCompras)
exibirLista(carrinhoPedido)
resultadoComFrete = calcularPedidoComFrete(carrinhoPedido)
print(f"O total é {resultadoComFrete.valorPedido}")
print(f"O frete é {resultadoComFrete.totalFrete}")
print(f"O numero de garrafas é {resultadoComFrete.quantidadeGarrafa}")
##print('LISTA Estoque')
##exibirLista(lista)

