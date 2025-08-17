Valor_total_compra=0
Valor_total_venda=0
cont=0
while cont<5:
    cont +=1
    Preco_De_Compra=int(input("Digite o preço de compra da escultura: "))
    Preco_De_Venda=int(input("Digite o preço de venda de sua escultura: "))
    if Preco_De_Compra:
        Valor_total_compra +=Preco_De_Compra
    if Preco_De_Venda:
        Valor_total_venda +=Preco_De_Venda
    coco=Preco_De_Venda-Preco_De_Compra
    if coco:
        print(f"O valor total do lucro individual dessa escultura é de: {coco}")
    

print(f"Media é igual a {(Valor_total_venda-Valor_total_compra)/5}")