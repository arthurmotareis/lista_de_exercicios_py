numero_de_0=0
soma_dos_numeros_positivos=0
media_dos_numeros_negativos=0
cont=0
while cont<6:
    num = int(input("Digite um numero inteiro: "))
    if num>0:
        print("O seu numero é positivo!")
    elif num<0:
        print("O seu numero é negativo!")
    else:
        print("O seu numero é igual a 0!")
    if num==0:
        numero_de_0 +=1
    cont +=1
    if num>0:
        soma_dos_numeros_positivos +=num
    if num<0:
        media_dos_numeros_negativos -=num
    
    


print(f"A quantidade de 0 que foram digitados é de: {numero_de_0}.\nA soma dos numeros inteiros positivos é de: {soma_dos_numeros_positivos}.\nA media dos numeros negativos é de: {(media_dos_numeros_negativos/cont)*-1}")


        
 



