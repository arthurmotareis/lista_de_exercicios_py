import sys
cont=0
nota=0
Nota_atual=0
maior_nota=0
while cont<5:
    nome=input("Digite seu nome: ")
    questoes_acertadas=int(input("Digite a quantidade de questões acertadas(0 a 10): "))
    if 10>=questoes_acertadas>=0:
        Nota_atual=questoes_acertadas*10
        nota +=Nota_atual

        print(f"O candidato {nome} tirou uma nota {questoes_acertadas*10} !!")
    else:
        sys.exit("A quantidade de questões acertadas é de 0 a 10!!!! ")
    if Nota_atual>maior_nota:
        maior_nota=Nota_atual
    cont +=1
print(f"A media das notas dos canditator é de: {nota/5}\nA maior nota foi: {maior_nota}")
