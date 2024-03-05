import json

def salvar_numero_em_json(numero):
    # Cria um dicionário com o número recebido
    dados = {"numero": numero}
    
    # Define o nome do arquivo
    nome_arquivo = "numero.json"
    
    # Abre o arquivo para escrita e salva os dados em formato JSON
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo)
    
    print(f"O número {numero} foi salvo em {nome_arquivo}.")

def main():
    numero = int(input("Digite um número: "))
    salvar_numero_em_json(numero)

if __name__ == "__main__":
    main()
