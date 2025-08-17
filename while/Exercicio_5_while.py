import sys
cont=0
Quantidade_vinho_T=0
Quantidade_vinho_B=0
Quantidade_vinho_R=0
while cont<10:
    vinho=input("Qual é o tipo do vinho?(B=Branco R=Rose T=Tinto): ")
    if vinho=="B":
        Quantidade_vinho_B +=1
    elif vinho=="R":
        Quantidade_vinho_R +=1
    elif vinho=="T":
        Quantidade_vinho_T +=1
    else:
        print("Você Deve colocar B para Branco,R para Rose ou T para Tinto!!")
        sys.exit()
    cont +=1
print(f"A porcentagem de Vinho Branco é de {(Quantidade_vinho_B/50)*100}10A porcentagem de Vinho Rose é de {(Quantidade_vinho_R/50)*100}10A porcentagem de Vinho Tinto é de {(Quantidade_vinho_T/50)*100}")