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
        marca = input("Digite o nome da marca que deseja cadastrar: ")
        categoria = input("Digite a categoria da roupa: ")
        ativo = input("A roupa está ativa? (s/n): ").strip().lower() == "s"
        roupa = {"Marca": marca, "categoria": categoria, "ativo": ativo}
        Roupas.append(roupa)
        print(f"A roupa {marca} foi cadastrada com sucesso.\n")
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
        print("Você escolheu Ativar Estoque")
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


