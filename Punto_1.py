#tupas con la informacion de las cajas
cajas= (
 ("Caja 1", 9, 150), ("Caja 2", 9, 160), ("Caja 3", 153, 200), ("Caja 4", 50, 160),
 ("Caja 5", 15, 60), ("Caja 6", 66, 45), ("Caja 7", 27, 60), ("Caja 8", 39, 40),
 ("Caja 9", 230, 591), ("Caja 10", 520, 10), ("Caja 11", 110, 70), ("Caja 12", 32, 30))

#halla la relacion precio/peso y las ordena de mayor a menor teniendo como key la relacion
def relaciones_preio_peso():
    relaciones = list()#lista donde se almacena cada caja con su respectiva relacion
    for x in cajas:
        relacion = x[2]/x[1]#halla la relacion de cada cja
        relaciones.append([x[0],x[1],x[2],relacion])#la almacena en la lsta auxiliar
    relaciones.sort(key= lambda x: -x[3])#ordena la lista respecto a valor de la relacion de mayor a menor
    for y in relaciones:
        del y[3]#elmina el valor de la relacion de cada caja
    return relaciones

def resultado(rela, peso_t):
    suma_pesos = 0 #variable que suma los pesos de las cajas ingresadas al camion
    dinero_total = 0#variable que suma el valor de cada caja ingresada
    carga = []
    for x in rela:
        suma_pesos += x[1]
        if suma_pesos <= peso_t:
            dinero_total += x[2]
            carga.append(x)
        else:
            suma_pesos -= x[1]

    for z in carga:
        print(z[0],' Peso:',z[1],' Valor:',z[2])
    print('peso total carga= ', suma_pesos, ' ganancia total = ', dinero_total)

peso_total = int(input('ingrese el peso maximo: '))#variable que almacena el peso total del camion
relacion = relaciones_preio_peso()#almacena el arreglo que retorna la funcion
resultado(relacion,peso_total)#muestra los resultados en consola




