class Conta:
     def __init__(self, nome, sexo, cpf, idade, ):
          self.nome = nome
          self.sexo = sexo
          self.cpf = cpf
          self.idade = idade

nome = str(input('Qual seu Nome: '))
print('Olá' + nome + 'Seja Bem vindo a Caixa Ecônomica Federal')
sexo = str(input('Qual é seu Genero: ' ))
idade = int(input('Qual a sua idade: '))
cpf = int(input('Digite seu cpf: '))