from funcoes import opcoes
from funcoes import consultar_estoque
from funcoes import vender_produto
from funcoes import repor_estoque
from funcoes import cadastrar_produto
from funcoes import ler_inteiro
from funcoes import relatorio

def menu():
    estoque = {}

    valores_validos = ["1", "2", "3", "4", "5", "6"]

    while True:
        try:
            opcao = opcoes()
            if opcao not in valores_validos:
                raise ValueError
            
            if opcao == "1":
                produto = input("Digite o produto que deseja consultar " )
                print(consultar_estoque(estoque,produto))
        
            
            elif opcao == "2":
                produto = input("Digite o produto que deseja vender " )
                quantidade = ler_inteiro("Digite a quantidade faturada. ")
                print(vender_produto(estoque,produto,quantidade))
            
            elif opcao == "3":
                produto = input("Digite o produto que deseja repor " )
                quantidade = ler_inteiro("Digite a quantidade. ")
                print(repor_estoque(estoque,produto,quantidade))
                
            elif opcao == "4":
                produto = input("Digite o produto que deseja cadastrar " )
                quantidade = ler_inteiro("Digite a quantidade. ")
                print(cadastrar_produto(estoque,produto,quantidade))
                
            elif opcao == "5":
                (relatorio(estoque))
            
                
            else:
                print("Finalizando")
                break
            
        
        
        except ValueError:
            print("Informe um valor válido. ")
            
if __name__ == "__main__":
    menu()

        
    