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

class SistemaBancario:
    def __init__(self):
        self.contas = []

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

    def menu(self):
        print('''[1] Criar Conta
[2] Acessar Conta
[3] Remover Conta
[4] Exibir Detalhes da Conta
[5] Sair''')

    def main(self):
        opcao = 0
        while opcao != 5:
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
                print('Finalizando...')
            else:
                print('Opção inválida. Tente novamente')
            print('=-=' * 10)

        print('Fim da Operação! Volte sempre')

if __name__ == "__main__":
    sistema_bancario = SistemaBancario()
    sistema_bancario.main()
