import random

#def ordenar(pri,p_pri,no_pri,p_no_pri):

def generar_numero(limite_sup,limite_inf,cantidad_datos):
    numeros_aleatorios =[]
    for x in range(0,int(cantidad_datos)):
        dato = random.randrange(limite_inf, limite_sup)
        if dato not in numeros_aleatorios:
            numeros_aleatorios.append(dato)
    return numeros_aleatorios

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




cantidad_datos = int(input('digite la cantidad de datos a ordenar: ',))
lim_sup = int(input('digite el limite superior:',))
lim_inf = int(input('digite el limite inferior:',))

numeros = generar_numero(lim_sup,lim_inf, cantidad_datos)
numeros.sort()
pos_pri = []
pos_no_pri = []
num_pri = []
num_no_pri = []

for x in range(len(numeros)):
    if es_primo(numeros[x]):
        num_pri.append(numeros[x])
        pos_pri.append(x)
    else:
        num_no_pri.append(numeros[x])
        pos_no_pri.append(x)

print(numeros)
print('*'*40)
print(pos_pri)
print(num_pri)
print('*'*40)
print(pos_no_pri)
print(num_no_pri)
print('*'*40)
conta = 0
x = 0
result = []
estado = False
num_pri.sort()
num_no_pri.sort()
num_pri.reverse()
# print('ordenados')
# print(pos_pri)
# print(num_pri)
# print('*'*40)
# print(pos_no_pri)
# print(num_no_pri)
# print('*'*40)
for n in num_no_pri:
    num_pri.append(n)
for p in pos_no_pri:
    pos_pri.append(p)

while x < len(pos_pri) and estado == False:
    if pos_pri[x] == conta:
        result.append(num_pri[x])
        x = 0
        conta += 1
        if conta == len(pos_pri) and len(result) == len(pos_pri) :
            estado = True
    else:
        x+=1

print(result)

