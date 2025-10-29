def opcoes():
    return input("1 - Consultar estoque\n"
                 "2 - Vender produto\n"
                 "3 - Repor estoque\n"
                 "4 - Cadastrar produto\n"
                 "5 - Relatório completo\n"
                 "6 - Encerrar\n").strip()
    

def consultar_estoque(dic,produto):
    if produto in dic:
        return f"Produto: {produto} | Quantidade: {dic[produto]} "
    else:
        return "Produto não encontrado. "
    
    
def vender_produto(dic,produto,quantidade):
    if produto in dic:
        if quantidade <= dic[produto]:
            dic[produto] -= quantidade
            return "Produto faturado!"
        else:
            return "Quantidade insuficiente!"
    else:
        return "Produto não cadastrado"

def repor_estoque(dic,produto,quantidade):
    if produto in dic:
        dic[produto] += quantidade
        return "Estoque atualizado"
    else:
        return "Produto não cadastrado"
    
def cadastrar_produto(dic,produto,quantidade):
    if produto not in dic:
        dic[produto] = quantidade
        return "Produto cadastrado com sucesso."
    else:
        return "Produto já cadastrado!"
    
def ler_inteiro(quantidade):
    while True:
        try:
            return int(input(quantidade))
        except ValueError:
            print("Informe um valor válido.")
                             
            
    
    
def relatorio(estoque):
    print("Relátorio do estoque:\n")
    for chave, quantidade in estoque.items():
        print(f"{chave}: {quantidade}")
        