import statistics

def suma_valorespos_yneg(list):
    suma_positivos = 0
    suma_negativos = 0

    for numero in list:
        numero = int(numero)
        if(numero>0):
            suma_positivos += numero

        else:
            suma_negativos += numero

    return suma_positivos, suma_negativos

lista = (89,-98,50,-48,-20,88,-100,80)

print(suma_valorespos_yneg(lista))

def potencia(numero, exponente):
    contador = 1  
    elevado = 1  

    while contador <= exponente:
        elevado = elevado * numero
        contador = contador + 1

    return elevado

print(potencia(2, 3)) 


def pares(list):
    lista0 = []
    for num in list: 
        if num % 2 == 0: 
            lista0.append(num)
            
    return lista0    
        

numeros = (2,3,4,8,9)
print(pares(numeros))

def numerosnegativos(list):
    lista01 = []
    for num in list:
        if num <0:
            lista01.append(num)

    return lista01

print(numerosnegativos(lista))






