class Conta:
    def __init__(self, nome, sexo, cpf, idade):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.idade = idade

def criar_conta():
    nome = input('Qual é o seu nome: ')
    print('Olá ' + nome + ', bem-vindo ao Banco XPTO!')
    sexo = input('Qual é o seu gênero: ')
    idade = int(input('Qual é a sua idade: '))
    cpf = input('Digite o seu CPF: ')
    senha = input('Digite a sua nova senha: ')
    numero_da_conta = 14563066  # Você pode querer gerar um número aleatório
    return Conta(nome, sexo, cpf, idade)

def acessar_conta(numero_da_conta, senha):


def remover_conta():

opcao = 0
while opcao != 4:
    print('''[1] Criar Conta
[2] Acessar Conta
[3] Remover Conta
[4] Sair''')
    opcao = int(input('Escolha a opção: '))

    if opcao == 1:
        nova_conta = criar_conta()
        print('Conta criada com sucesso!')

    elif opcao == 2:
        numero_conta = input('Digite o número da conta: ')
        senha = input('Digite a sua senha: ')
        acessar_conta(numero_conta, senha)

    elif opcao == 3:
        remover_conta()

    elif opcao == 4:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)

print('Fim da Operação! Volte sempre')
