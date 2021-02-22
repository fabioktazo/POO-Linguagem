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
  def __init__ (self, logradouro, numero, bairro, complemento, cidade, cep)
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

class Funcionario (Pessoa)