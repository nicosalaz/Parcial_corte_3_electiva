import random
#genera numeros aleatorios desde un limite inferior hasta un limite superios una n catidad de numeros
def generar_numero(limite_sup,limite_inf,cantidad_datos):
    numeros_aleatorios =[]
    conta = 0
    while conta < int(cantidad_datos):
        dato = random.randrange(limite_inf, limite_sup)
        if dato not in numeros_aleatorios:
            numeros_aleatorios.append(dato)
            conta+=1
    return numeros_aleatorios
#funcion que verifica si un numero es primo o no
def es_primo(n):
    conta = 0
    if n == 0 :
        return False
    elif n == 1:
        return True
    else:
        for x in range(2,n):
            if n % x == 0:
                conta += 1
        if conta != 0:
            return False
        else:
            return True

#funcion que recibe dos arreglos uno con las posiciones y otro con los numeros generados
def ordenar_arreglo(pos, num):
    conta = 0 #variable que me indica cual es la posicion que voy a ingresar
    x = 0 #variable iteradora que controla el paso del ciclo while
    result = [] # arreglo donde se almacenaran los resutados
    estado = False #variable que me controla el paso del ciclo while
    while x < len(pos) and estado == False:
        if pos[x] == conta:
            result.append(num[x])
            x = 0
            conta += 1
            if conta == len(pos) and len(result) == len(pos):
                estado = True
        else:
            x += 1

    print(result)
#funcion que divide los numeros y sus posiciones en arreglos de primos y no primos
def division_numeros(numeros):
    pos_pri = [] #arreglo que almacena la posicion de los primos del arreglo original ordenado
    pos_no_pri = [] #arreglo que almacena la posicion de los no primos del arreglo original ordenado
    num_pri = [] #arreglo que almacena los numeros primos del arreglo original ordenado
    num_no_pri = [] #arreglo que almacena los numeros no primos del arreglo original ordenado
    #ciclo que me llena cada uno de los arreglos, determinando si es primo o no
    for x in range(len(numeros)):
        if es_primo(numeros[x]):
            num_pri.append(numeros[x])
            pos_pri.append(x)
        else:
            num_no_pri.append(numeros[x])
            pos_no_pri.append(x)

    print(numeros)
    print('*' * 40)
    # ordeno los arreglos 
    num_pri.sort()
    num_pri.reverse()
    num_no_pri.sort()
    #uno los numeros en un solo arreglo y las posiciones en otro
    for n in num_no_pri:
        num_pri.append(n)
    for p in pos_no_pri:
        pos_pri.append(p)

    return num_pri,pos_pri


cantidad_datos = int(input('digite la cantidad de datos a ordenar: ',))
lim_sup = int(input('digite el limite superior:',))
lim_inf = int(input('digite el limite inferior:',))

numeros = generar_numero(lim_sup,lim_inf, cantidad_datos)
print(numeros)
print('*'*40)
numeros.sort()

nums,posiciones = division_numeros(numeros)

ordenar_arreglo(posiciones,nums)

