import json

class Conta:
    def __init__(self, nome, sexo, cpf, idade, numero_da_conta, senha, saldo=0):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.idade = idade
        self.numero_da_conta = numero_da_conta
        self.senha = senha
        self.saldo = saldo

    def __str__(self):
        return f"Nome: {self.nome}, Sexo: {self.sexo}, CPF: {self.cpf}, Idade: {self.idade}, Número da Conta: {self.numero_da_conta}"

    def ver_saldo(self):
        print("Saldo: R$ ", self.saldo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Operação Concluída com sucesso!')
        else:
            print('Saldo Insuficiente')

    def depositar(self, valor):
        self.saldo += valor
        print('Depósito concluído com sucesso!')

    def alterar_senha(self, senha_antiga, senha_nova):
        if self.senha == senha_antiga:
            self.senha = senha_nova
            print("Senha alterada com Sucesso!")
        else:
            print("Senhas não correspondem")

class SistemaBancario:
    def __init__(self):
        self.contas = []

    def carregar_contas_do_json(self):
        try:
            with open("contas.json", "r") as arquivo:
                dados_contas = json.load(arquivo)
                for dados_conta in dados_contas:
                    conta = Conta(dados_conta["nome"], dados_conta["sexo"], dados_conta["cpf"], dados_conta["idade"], dados_conta["numero_da_conta"], dados_conta["senha"], dados_conta.get("saldo", 0))
                    self.contas.append(conta)
            print("Contas carregadas com sucesso!")
        except FileNotFoundError:
            print("Nenhum arquivo de contas encontrado.")

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
        self.salvar_contas_em_json()

    def salvar_contas_em_json(self):
        dados_contas = []
        for conta in self.contas:
            dados_conta = {
                "nome": conta.nome,
                "sexo": conta.sexo,
                "cpf": conta.cpf,
                "idade": conta.idade,
                "numero_da_conta": conta.numero_da_conta,
                "senha": conta.senha,
                "saldo": conta.saldo
            }
            dados_contas.append(dados_conta)

        with open("contas.json", "w") as arquivo:
            json.dump(dados_contas, arquivo)
        print(f"Todas as contas foram salvas em contas.json")

    def acessar_conta(self):
        numero_conta = int(input('Digite o número da conta: '))
        senha = input('Digite a sua senha: ')
        for conta in self.contas:
            if conta.numero_da_conta == numero_conta and conta.senha == senha:
                print('Acesso permitido!')
                self.menu_conta(conta)
                self.salvar_contas_em_json()  # Salvar após cada operação de conta
                return conta
        print('Número da conta ou senha incorretos.')
        return None

    def remover_conta(self):
        numero_conta = int(input('Digite o número da conta a ser removida: '))
        for i, conta in enumerate(self.contas):
            if conta.numero_da_conta == numero_conta:
                del self.contas[i]
                print('Conta removida com sucesso!')
                self.salvar_contas_em_json()
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

    def exibir_todas_contas(self):
        if self.contas:
            print("Todas as contas:")
            for conta in self.contas:
                print(conta)
        else:
            print("Nenhuma conta encontrada.")

    def menu(self):
        print('''[1] Criar Conta
[2] Acessar Conta
[3] Remover Conta
[4] Exibir Detalhes da Conta
[5] Exibir Todas as Contas
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
                self.exibir_todas_contas()

            elif opcao == 6:
                print('Finalizando...')
            else:
                print('Opção inválida. Tente novamente')
            print('=-=' * 10)

        print('Fim da Operação! Volte sempre')

    def Menu_minha_conta(self):
        print('''[1] Ver Saldo
[2] Sacar
[3] Depositar
[4] Ver Informações do Cliente
[5] Alterar Senha
[6] Sair ''')

    def menu_conta(self, conta):
        opcao = 0
        while opcao != 6:
            self.Menu_minha_conta()
            opcao = int(input('Escolha a opção: '))

            if opcao == 1:
                conta.ver_saldo()

            elif opcao == 2:
                valor = float(input('Digite o valor à ser sacado: '))
                conta.sacar(valor)
                self.salvar_contas_em_json()

            elif opcao == 3:
                valor = float(input('Digite o valor à ser depositado: '))
                conta.depositar(valor)
                self.salvar_contas_em_json()

            elif opcao == 4:
                self.ver_informacoes()

            elif opcao == 5:
                senha_antiga = input('Digite sua senha atual: ')
                senha_nova = input('Digite sua senha nova: ')
                conta.alterar_senha(senha_antiga, senha_nova)
                self.salvar_contas_em_json()

            elif opcao == 6:
                print('Finalizando...')
            else:
                print('Opção inválida. Tente novamente')
            print('=-=' * 10)

if __name__ == "__main__":
    sistema_bancario = SistemaBancario()
    sistema_bancario.carregar_contas_do_json()
    sistema_bancario.main()
