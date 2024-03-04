import json
import os

class Conta:
    def __init__(self, nome, sexo, cpf, idade, numero_da_conta, senha):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.idade = idade
        self.numero_da_conta = numero_da_conta
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, Sexo: {self.sexo}, CPF: {self.cpf}, Idade: {self.idade}, Número da Conta: {self.numero_da_conta}"

    def to_json(self):
        return {
            "nome": self.nome,
            "sexo": self.sexo,
            "cpf": self.cpf,
            "idade": self.idade,
            "numero_da_conta": self.numero_da_conta,
            "senha": self.senha
        }

class SistemaBancario:
    def __init__(self):
        self.contas = []
        self.arquivo_json = 'contas.json'
        self.carregar_contas()

    def carregar_contas(self):
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, 'r') as file:
                dados = json.load(file)
                for dado in dados:
                    conta = Conta(**dado)
                    self.contas.append(conta)
            print('Dados das contas carregados com sucesso!')
        else:
            print('Arquivo JSON de contas não encontrado. Criando novo arquivo.')

    def criar_conta(self):
        nome = input('Qual é o seu nome: ')
        print('Olá ' + nome + ', bem-vindo ao Banco XPTO!')
        sexo = input('Qual é o seu gênero: ')
        idade = int(input('Qual é a sua idade: '))
        cpf = input('Digite o seu CPF: ')
        numero_da_conta = int(input('Digite o número da conta: '))
        senha = input('Digite a sua nova senha: ')
        conta = Conta(nome, sexo, cpf, idade, numero_da_conta, senha)
        self.contas.append(conta)
        print('Conta criada com sucesso!')

    def acessar_conta(self):
        numero_conta = int(input('Digite o número da conta: '))
        senha = input('Digite a sua senha: ')
        for conta in self.contas:
            if conta.numero_da_conta == numero_conta and conta.senha == senha:
                print('Acesso permitido!')
                return
        print('Número da conta ou senha incorretos.')

    def remover_conta(self):
        numero_conta = int(input('Digite o número da conta a ser removida: '))
        for i, conta in enumerate(self.contas):
            if conta.numero_da_conta == numero_conta:
                del self.contas[i]
                print('Conta removida com sucesso!')
                return
        print('Número da conta não encontrado.')

    def exibir_detalhes_conta(self):
        numero_conta = int(input('Digite o número da conta: '))
        for conta in self.contas:
            if conta.numero_da_conta == numero_conta:
                print('Detalhes da Conta:')
                print(conta)
                return
        print('Conta não encontrada.')

    def salvar_contas_json(self):
        with open(self.arquivo_json, 'w') as file:
            json.dump([conta.to_json() for conta in self.contas], file, indent=4)
        print(f'Dados das contas salvos em {self.arquivo_json}')

    def menu(self):
        print('''[1] Criar Conta
[2] Acessar Conta
[3] Remover Conta
[4] Exibir Detalhes da Conta
[5] Salvar Contas em JSON
[6] Sair''')

    def main(self):
        opcao = 0
        while opcao != 6:
            self.menu()
            opcao = int(input('Escolha a opção: '))

            if opcao == 1:
                self.criar_conta()

            elif opcao == 2:
                self.acessar_conta()

            elif opcao == 3:
                self.remover_conta()

            elif opcao == 4:
                self.exibir_detalhes_conta()

            elif opcao == 5:
                self.salvar_contas_json()

            elif opcao == 6:
                print('Finalizando...')
            else:
                print('Opção inválida. Tente novamente')
            print('=-=' * 10)

        print('Fim da Operação! Volte sempre')


if __name__ == "__main__":
    sistema_bancario = SistemaBancario()
    sistema_bancario.main()
