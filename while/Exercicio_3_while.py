
Quantidade_De_Maior_Idade_Mulher=0
Homens_Brasileiros_Entre_20_a_30_anos=0
Media_das_idades=0
cont=0
while cont<15:
    Sexo=input("Digite seu sexo(F para mulher M para homem): ")
    if Sexo=="F":
        Idade_Mulher=int(input("Digite sua idade: "))
        Nacionalidade_Mulher=input("Digite sua nacionalidade: ")
        Media_das_idades +=Idade_Mulher
    elif Sexo=="M":
        Idade_Homem=int(input("Digite sua idade: "))
        Nacionalidade_Homem=input("Digite sua nacionalidade: ")
        Media_das_idades +=Idade_Homem
    elif Sexo !="F" and Sexo != "M":
        raise Exception("Digite apenas F para Mulher e M para Homem.")
    if Sexo=="M":
        if Idade_Homem>=20<=30:
            if Nacionalidade_Homem=="Brasileiro":
                Homens_Brasileiros_Entre_20_a_30_anos +=1
    if Sexo=="F":
        if Idade_Mulher>=18:
            Quantidade_De_Maior_Idade_Mulher +=1
    cont +=1
print(f"A quantidade de Mulheres maiores de 18 anos é de: {Quantidade_De_Maior_Idade_Mulher}\nA quantidade de homens brasileiros entre 20 a 30 anos é igual á: {Homens_Brasileiros_Entre_20_a_30_anos}\nA media das idades de homens e mulheres é de: {Media_das_idades/15}")