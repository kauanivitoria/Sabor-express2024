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
    print("1. Cadastrar Roupa")
    print("2. Listar Roupas")
    print("3. Ativar Estoque")
    print("4. Sair")

def escolhe_opcao():
    def exibir_subtitulo(texto):
        os.system("cls" if os.name == "nt" else "clear")
        linha = "_" * 65
        print(linha)
        print(texto)
        print(linha)
        print(" ")

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastra_Roupa():
        exibir_subtitulo("Cadastrar Roupas")
        marca_Roupa = input("Digite o nome da marca que deseja cadastrar: ")
        categoria_Roupa = input(f"Digite a categoria da roupa {marca_Roupa}: ")
        dados_da_Roupa = {"Marca": marca_Roupa, "categoria": categoria_Roupa, "ativo": True}
        Roupas.append(dados_da_Roupa)
        print(f"A roupa {marca_Roupa} foi cadastrada com sucesso\n")
        retorna_menu()

    def listar_Roupas():
        exibir_subtitulo("Lista de Roupas Cadastradas")
        for roupa in Roupas:
            marca_Roupa = roupa["Marca"]
            categoria_Roupa = roupa["categoria"]
            ativo = "Com estoque" if roupa["ativo"] else "Sem estoque"
            print(f" - {marca_Roupa.ljust(20)} | {categoria_Roupa.ljust(20)} | {ativo}")
        retorna_menu()

    def ativar_Estoque():
        exibir_subtitulo("Ativar Estoque")
        marca_Roupa = input("Digite o nome da roupa que deseja ativar: ")
        roupa_encontrada = False

        for roupa in Roupas:
            if marca_Roupa == roupa["Marca"]:
                roupa_encontrada = True
                roupa["ativo"] = not roupa["ativo"]
                mensagem = f"{marca_Roupa} foi ativado com sucesso" if roupa["ativo"] else f"A roupa {marca_Roupa} foi desativada"
                print(mensagem)
                break
        if not roupa_encontrada:
            print("Roupa não encontrada")
        retorna_menu()

    def finalizar_programa():
        os.system("cls" if os.name == "nt" else "clear")
        print("Finalizando o programa\n")

    def opcao_invalida():
        print("Essa opção não é válida")
        input("Aperte qualquer tecla para voltar")
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastra_Roupa()
        elif opcao_escolhida == 2:
            listar_Roupas()
        elif opcao_escolhida == 3:
            ativar_Estoque()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()
