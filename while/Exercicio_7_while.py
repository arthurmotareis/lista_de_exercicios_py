cont = 0 
Peso_maior=0
while cont < 10:
    Peso = float(input("Digite O peso em kilos: "))
    if Peso>Peso_maior:
        Peso_maior=Peso
    cont +=1
print(f"O mair peso é {Peso_maior} !!")