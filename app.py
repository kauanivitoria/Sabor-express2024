import os

Roupas = [
    {"Marca": "milliur", "categoria": "casual", "ativo": True},
    {"Marca": "Pit-Bull", "categoria": "alto Padrão", "ativo": False},
    {"Marca": "cropt", "categoria": "alfaiataria", "ativo": True}
]

def mostra_titulo():
    print("""
      
██╗░░░██╗██╗████████╗░█████╗░██████╗░██╗░█████╗░  ███╗░░░███╗░█████╗░██████╗░░█████╗░░██████╗
██║░░░██║██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝
╚██╗░██╔╝██║░░░██║░░░██║░░██║██████╔╝██║███████║  ██╔████╔██║██║░░██║██║░░██║███████║╚█████╗
░╚████╔╝░██║░░░██║░░░██║░░██║██╔══██╗██║██╔══██║  ██║╚██╔╝██║██║░░██║██║░░██║██╔══██║░╚═══██╗
░░╚██╔╝░░██║░░░██║░░░╚█████╔╝██║░░██║██║██║░░██║  ██║░╚═╝░██║╚█████╔╝██████╔╝██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚═════╝
    """)

def mostra_escolhas():
    print("1. Cadastrar Roupas")
    print("2. Listar Roupas")
    print("3. Ativar Estoque")
    print("4. Sair")

def escolhe_opcao():
    def exibir_subtitulo(texto):
        os.system("cls" if os.name == "nt" else "clear")
        print(texto)
        print(" ")
      
    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()
    
    def cadastrar_roupas():
        exibir_subtitulo("Cadastrar Roupa")

        marca_roupas = input("Digite a marca da roupa que deseja cadastrar: ")
        categoria_roupas = input("Digite a categoria que deseja cadastrar: ")
        dados_da_roupa = {"Marca": marca_roupas, "categoria": categoria_roupas, "ativo": True}
        Roupas.append(dados_da_roupa)
        retorna_menu()
    
    def listar_roupas():
        exibir_subtitulo("Lista de Roupas Cadastradas")
        if not Roupas:
            print("Nenhuma roupa cadastrada.")
        else:
            for roupa in Roupas:
                marca = roupa["Marca"]
                categoria = roupa["categoria"]
                ativo = "Sim" if roupa["ativo"] else "Não"
                print(f" - {marca} | {categoria} | {ativo}")
        retorna_menu()
    
    def ativar_estoque():
        exibir_subtitulo("Ativar Estoque")
        marca_roupas = input("Digite o nome da marca que deseja ativar: ")
        marca_encontrada = False

        for roupa in Roupas:
            if roupa["Marca"] == marca_roupas:
                marca_encontrada = True
                roupa["ativo"] = not cliente ["ativo"]
                mensagem = f"o cadastro do {Roupas} foi ativado/desativado com sucesso" if

        if not marca_encontrada:
            print(f"Marca {marca_roupas} não encontrada.")
        retorna_menu()
    
    def finalizar_programa():
        os.system("cls" if os.name == "nt" else "clear") 
        print("Finalizando o programa\n") 
        exit()
    
    def opcao_invalida():
        print("Opção inválida. Tente novamente.")
        input("Aperte qualquer tecla para voltar")
        main()  
    
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_roupas()
        elif opcao_escolhida == 2:
            listar_roupas()
        elif opcao_escolhida == 3:
            ativar_estoque()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        input("Aperte qualquer tecla para voltar")
        main()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()
