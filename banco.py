# Essa é uma classe POO
class Conta:
    def __init__(self, nome, sexo, cpf, idade, senha, numero_da_conta):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.idade = idade
        self.senha = senha
        self.numero_da_conta = numero_da_conta

# Defenir a função criar conta
def criar_conta():
    nome = str (input('Qual é o seu nome: '))
    print('Olá ' + nome + ', bem-vindo ao Banco XPTO!')
    sexo = str (input('Qual é o seu gênero: '))
    idade = int (input('Qual é a sua idade: '))
    cpf = int (input('Digite o seu CPF: '))
    senha = int (input('Digite a sua nova senha: '))
    numero_da_conta = int (input('Digite o numero da conta'))
    return Conta(nome, sexo, cpf, idade, senha, numero_da_conta)

# Defenir a função acessar conta
def acessar_conta(numero_da_conta, senha):
    numero_conta = int (input('Digite o numero da conta: '))
    senha = int (input('Digite sua senha: '))
    return Conta(numero_da_conta, senha)

# Definir a função remover conta
def remover_conta(numero_da_conta, senha ):
    print(f'Remover Conta')

# Lógica de while com combinação if elif e else
# Acesso ao Menu Principal    
opção = 0
while opção != 4:
    print('''[1] Criar Conta
[2] Acessar Conta
[3] Remover Conta
[4] Sair''')
    opção = int(input('Escolha a opção: '))

    if opção == 1:
        nova_conta = criar_conta()
        print('Conta criada com sucesso!')

    elif opção == 2:
        acessar = acessar_conta()
        print('Seja bem vindo a Caixa Economica federal! ')

    elif opção == 3:
        remover_conta()

    elif opção == 4:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)

print('Fim da Operação! Volte sempre')
