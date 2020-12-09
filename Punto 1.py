cajas= (
 ("Caja 1", 9, 150), ("Caja 2", 9, 160), ("Caja 3", 153, 200), ("Caja 4", 50, 160),
 ("Caja 5", 15, 60), ("Caja 6", 66, 45), ("Caja 7", 27, 60), ("Caja 8", 39, 40),
 ("Caja 9", 230, 591), ("Caja 10", 520, 10), ("Caja 11", 110, 70), ("Caja 12", 32, 30))

peso1 = 0
peso2 = 0
valor1 = 0
valor2 = 0
carga = []
for x in range(1):
    for y in range(len(cajas)):
        print(cajas[y][x], "Peso: ",cajas[y][x+1],"Valor: ", cajas[y][x+2])

valorPeso = 750
for x in range(1):
    for y in range(len(cajas)):
        if peso1 < peso2 and valor1>valor2:
            carga = carga.append(cajas(y))