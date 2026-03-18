def list_shift(lista, valor):
    for i in range(len(lista)):
        lista[i] += valor

def calc_avg(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma / len(lista)

def print_normalized(lista):
    print(lista)

datos = [2.0, 4.0, 6.0, 8.0]

prom = calc_avg(datos)
list_shift(datos, -prom)
print_normalized(datos)