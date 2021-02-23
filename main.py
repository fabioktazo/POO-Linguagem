class Pessoa:
  def __initt__ (self, nome, contato, id, estrelas):
    self.nome = nome
    self.contato = contato
    self.id =  id
    self.estrelas = estrelas
  def abrir_perfil(self):
    os.system('clear')
    print ("PERFIL DE: ", self.nome)
    print ("CONTATO: ", self.contato)
  def enviar_mensagem(self):
    menssagem = input ("DIGITE A MENSAGEM A SER ENVIADA: ")
    print ("SUA MENSAGEM FOI ENVIADA COM SUCESSO!")

class Endereco:
  def __init__ (self, logradouro, numero, bairro, complemento, cidade, cep):
    self.logradouro = logradouro
    self.numero = numero
    self.bairro = bairro
    self.complemento = complemento
    self.cidade = cidade
    self.cep = cep
  def cadastrar_endereco (self):
    self.Endereco()
  def alterar_endereco (self):
    self.Endereco()

class Cliente (Pessoa):
  def __init__ (self, nome, contato, id, estrelas, cpf):
    super().__init__(nome, contato, id, estrelas)
    self.cpf = cpf
    endereco = Endereco()
    forma_pagamento = 0
  def cancelar_pedido(self):
    print ("SEU PEDIDO FOI CANCELADO COM SUCESSO!")
  def confirmar_pedido(self):
    confirmacao = input ("VOCÊ DESEJA CONFIRMAR O(S) SEU(S) PEDIDO(S)? ")
    if confimacao == "sim" or "Sim" or "SIM":
      print ("PEDIDO(S) CONFIMADO COM SUCESSO! AGRADECEMOS A PREFERÊNCIA!")
      return True
    else:
      return False
  def informar_atraso(self):
    print ("ALERTA DE ATRASO ENVIADO COM SUCESSO!")
  def avaliar_entregador(self):
    avaliacao_entregador = input (float ("DIGITE A AVALIAÇÃO DO ENTREGADOR (DE 0.0 a 5.0): "))
    return avaliacao_entregador
  def avaliar_restaurante(self):
    avaliacao_restaurante = input (float ("DIGITE A AVALIAÇÃO DO RESTAURANTE (DE 0.0 a 5.0): "))
    return avaliacao_restaurante

class Funcionario (Pessoa):
  def __init__ (self, data_admissao, cargo, cpf_funcionario, nome, contato, id, estrelas):
    super().__init__(nome, contato, id, estrelas)
    self.data_admissao = data_admissao
    self.cargo = cargo
    self. cpf_funcionario = cpf_funcionario
  def liberar_pedido (self):
    confirmar = input ("VOCÊ DESEJA CONFIRMAR O(S) PEDIDO(S)?")
    if confirmar == "sim" or "SIM" or "Sim":
      print("PEDIDO(S) CONFIRMADO(S) COM SUCESSO! AGRADECEMOS A PREFERÊNCIA.")
      return True
    else:
      return False
  def registrar_entrada (self):
    print("ENTRAGA REGISTRADA COM SUCESSO!")
  def registrar_saida (self):
    print("SAÍDA REGISTRADA COM SUCESSO!")

class Cardapio:
  def __init__ (self):
    self.cardapio = []
  def exibir_cardapio (self):
    self.cardapioescolha = ["SUSHI TRADICIONAL", "HOSOMAKI", "MAKIZUSHI", "TEMAKI", "URUMAKI", "NIGUIRI", "SASHIMI", "HOT FILADÉLFIA", "TEMPURÁ", "YAKISOBA TRADICIONAL", "YAKISOBA VEGANO", "HARUMAKI", "MOYASHI", "MOCHI", "MANJU"]

    for x in range (len(self.cardapioescolha)):
      print (x+1, "-", self.cardapioescolha[x])
    print ("16 - ENCERRAR PEDIDOS E PROSSEGUIR")
    a = input ("DIGITE O NÚMERO CORRESPONDENTE AO SEU PEDIDO (OBS.: VOCÊ PODERÁ ESCOLHER MAIS DE UM PEDIDO DESDE SELECIONE UM DE CADA VEZ): ")
    if a == "1":
      os.system('clear')
      self.cardapioescolha.append(sushi_tradicional)
      self.exibir_cardapio()
    if a == "2":
      os.system('clear')
      self.cardapioescolha.append(hosomaki)
      self.exibir_cardapio()
    if a == "3":
      os.system('clear')
      self.cardapioescolha.append(makizushi)
      self.exibir_cardapio()
    if a == "4":
      os.system('clear')
      self.cardapioescolha.append(temaki)
      self.exibir_cardapio()
    if a == "5":
      os.system('clear')
      self.cardapioescolha.append(urumaki)
      self.exibir_cardapio()
    if a == "6":
      os.system('clear')
      self.cardapioescolha.append(niguiri)
      self.exibir_cardapio
    if a == "7":
      os.system('clear')
      self.cardapioescolha.append(sashimi)
      self.exibir_cardapio()
    if a == "8":
      os.system('clear')
      self.cardapioescolha.append(hot_filadelfia)
      self.exibir_cardapio()
    if a == "9":
      os.system('clear')
      self.cardapioescolha.append(tempura)
      self.exibir_cardapio()
    if a == "10":
      os.system('clear')
      self.cardapioescolha.append(yakisoba_tradicional)
      self.exibir_cardapio()
    if a == "11":
      os.system('clear')
      self.cardapioescolha.append(yakisoba_vegano)
      self.exibir_cardapio
    if a == "12":
      os.system('clear')
      self.cardapioescolha.append(harumaki)
      self.exibir_cardapio()
    if a == "13":
      os.system('clear')
      self.cardapioescolha.append(moyashi)
      self.exibir_cardapio() 
    if a == "14":
      os.system('clear')
      self.cardapioescolha.append(mochi)
      self.exibir_cardapio() 
    if a == "15:
      os.system('clear')
      self.cardapioescolha.append(manju)
      self.exibir_cardapio() 
    elif a == "16":
      os.system('clear')
      menu = Menu()
      menu.remover_produto_cardapio()
    else:
      os.system('clear')
      print("ERRO")
      self.exibir_cardapio() 
global cardapio

class Carrinho:
  def __init__(self):
    self.id_venda = id_venda
    self.cardapio = Cardapio()
    self.endereco_entrega = Endereco()
  def remover_produto(self):
    produto = None
  def cancelar_pedido(self):
    print("PEDIDO CANCELADO!")
  def confirmar_pedido1(self):
    confirmacao1 = input ("VOCE DESEJA CONFIRMA O(S) SEU(S) PEDIDO(S)? ")
    if confimacao1 == "sim" or "SIM" or "Sim":
      print("SEU PEDIDO FOI CONFIRMARDO! AGRADECEMOS A PREFERÊNCIA")
      return True
    else:
      return False

class Produtos:
  def __init__(self, preco_produto, id_produto, tipo_ProdutoSalgado):
    self.preco_produto = preco_produto
    self.id_produto = id_produto
    self.tipo_ProdutoSalgado = tipo_ProdutoSalgado
  def cadastrar_produto(self):
    self.produto = input ("DIGITE O NOME DO PRODUTO A SER CADASTRADO: ")
    print("PRODUTO CADASTRADO COM SUCESSO!")
  def alterar_produto(self):
    self.produto = input ("DIGITE O NOVO PRODUTO: ")
    print("PRODUTO ALTERADO COM SUCESSO!")
  def adicionar_produto_estoque(self):
    produto_estoque = input ("DIGITE O NOME DO PRODUTO A SER ACRESCENTADO NO ESTOQUE: ")
    print("PRODUTO ADICIONADO COM SUCESSO!")
  def remover_produto_estoque(self):
    produto_estoque = None

sushi_tradicional = Produtos(3.00, 1, True)
hosomaki = Produtos(3.00, 2, True)
makizushi = Produtos(3.50, 3, True)
temaki = Produtos(5.00, 4, True)
urumaki = Produtos(3.50, 5, True)
niguiri = Produtos(8.00, 6, True)
sashimi = Produtos(5.00, 7, True)
hot_filadelfia = Produtos(4.00, 8, True)
tempura = Produtos(5.00, 9, True)
yakisoba_tradicional = Produtos(47.90, 10, True)
yakisoba_vegano = Produtos(48.00, 11, True)
harumaki = Produtos(10.00, 12, True)
moyashi = Produtos(20.00, 13, True)
mochi = Produtos(5.00, 14, False)
manju = Produtos(6.00, 15, False)

