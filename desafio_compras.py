def menu(): #Menu de comprar criado como funcao pra sempre ficar rodando por isso () 
    print("\n≣≣≣≣≣ MENU ≣≣≣≣")
    print("1 - Adicionar no carrinho")
    print("2 - Visualizar items do carrinho")
    print("3 - Remover items do carrinho")
    print("0 - Sair")


def main(): #Funcao principal que ira rodar toda condicional 
    
    produtos = [] #Lista para armazenar 
    proximo_id = 1

    while True:
        menu()
        opcao = input("Escolha: ").strip()

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            print("Você escolheu adicionar um novo produto no carrinho! ")

            produto = (input("Digite o nome do produto a ser adicionado: "))
            criacao = {                      #Criacao de dicionario guarada por id 
                "id": proximo_id,
                "nome": produto,
            }

            produtos.append(criacao)

            proximo_id += 1 #verificacao pra sempre adicionar um 1 referente a base
            
        elif opcao == "2":

            if not produtos: #Verificacao se a lista esta vazia
                print("Lista está vazia...")
            else:
                print("\n≣≣≣≣≣ Carrinho ≣≣≣≣")
                for indice,produto in enumerate(produtos): #Percorer o indice e o produto referente a tal e enumerar os produtos 
                    print(f"Nome: {produto["nome"]}")

        elif opcao == "3":
            print("Você escolheu deletar um produto do seu carrinho...")
            achou = False 

            delet_usuario = (input("Digite o nome do produto desejado para deletar..."))
                  
            for produto in produtos:
                if produto["nome"] == delet_usuario:
                    achou = True
                    break

            if not achou: print("Produto nao encontrado...")

            if produto["nome"] == delet_usuario:
                condicao_usuario = input(f"Vocé deseja excluir {produto["nome"]} ? ").lower().strip()
                if condicao_usuario == "sim":
                    produtos.remove(produto)
                elif condicao_usuario == "nao":
                    print("Operaçao cancelada...")
            
       



        else:
            print("Opção inválida!")


main()
# ██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ██╗      ██████╗ ███╗   ██╗███████╗
# ██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔══██╗██║     ██╔═══██╗████╗  ██║██╔════╝
# ██████╔╝ ╚████╔╝     ██╔████╔██║███████║██║     ██║   ██║██╔██╗ ██║█████╗
# ██╔══██╗  ╚██╔╝      ██║╚██╔╝██║██╔══██║██║     ██║   ██║██║╚██╗██║██╔══╝
# ██████╔╝   ██║       ██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║███████╗
# ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
#
#                 >>> CODED BY MALONE <<<
#              [ SYSTEM CODARA INTERFACE ]