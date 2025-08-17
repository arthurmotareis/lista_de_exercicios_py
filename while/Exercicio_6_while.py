cont = 0
menor_imc = None

while cont < 10:
    Altura = float(input("Digite sua altura em metros: "))
    Peso = float(input("Digite seu peso em kilos: "))
    
    IMC = Peso / (Altura ** 2)
    print(f"Seu IMC é {IMC} !!")
    
    if IMC < 18.5:
        print("Abaixo do peso !!")
    elif 18.5 <= IMC < 25:
        print("Peso normal !!")
    elif 25 <= IMC < 30:
        print("Acima do peso !!")
    else:
        print("Obesidade !!")
    
    if menor_imc is None or IMC < menor_imc:
        menor_imc = IMC
    
    cont += 1

print(f"O menor IMC digitado foi: {menor_imc}")
