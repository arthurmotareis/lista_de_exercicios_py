Pessoas_Que_assistiram_contagem=0
Gostou_contagem=0
Não_Gostou_contagem=0
cont=0
while cont<15:
    Pessoas_Que_assistiram=input("Você assistiu a apresentação?(Sim ou Não): ")
    if Pessoas_Que_assistiram=="Sim":
        Pessoas_Que_assistiram_contagem +=1
    elif Pessoas_Que_assistiram=="Não":
        continue
    else:
        raise Exception("Você Deve usar apenas Sim ou Não")
    Gostou_ou_Não_Gostou=input("Você gostou da apresentação?(Sim ou Não): ")
    if Gostou_ou_Não_Gostou=="Sim":
        Gostou_contagem +=1
    elif Gostou_ou_Não_Gostou=="Não":
        Não_Gostou_contagem +=1
    else:
        raise Exception("Use apenas Sim ou Não")
    cont +=1
if Gostou_contagem==Não_Gostou_contagem:
    print("Deu empate entra as pessoas que gostaram e as que nao gostaram.")
elif Gostou_contagem>Não_Gostou_contagem:
    print("A maioria das pessoas gostaram da apresentação.")
else:
    print("A maioria das pessoas não gostaram da apresentação.")
        
    