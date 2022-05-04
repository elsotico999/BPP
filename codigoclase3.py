import statistics

class funciones:
    """Esta es una primera descripción de la clase.
    """
    def suma_valorespos_yneg(list):
        """Esta es una función que suma de una lista, los valores positivos por un lado y los valores negativos por otro.
        
        -parámetro: list.
        
        -type in list: `int`.
        """
        suma_positivos = 0
        suma_negativos = 0

        for numero in list:
            numero = int(numero)
            if(numero>0):
                suma_positivos += numero

            else:
                suma_negativos += numero

        return suma_positivos, suma_negativos

    def potencia(numero, exponente):
        """Esta es una función que eleva un número a una potencia dada.
        
        -parámetros: numero y exponente.
        
        -type numero: `int`.
        
        -type exponente: `int`.
        """
        contador = 1  
        elevado = 1  

        while contador <= exponente:
            elevado = elevado * numero
            contador = contador + 1

        return elevado


    def pares(list):
        """Esta es una función que selecciona y nos da como resultado los números pares de una lista.
        
        -parámetro: list.
        
        -type in list: `int`.
        """
        lista0 = []
        for num in list: 
            if num % 2 == 0: 
                lista0.append(num)
            
        return lista0    
        

    def numerosnegativos(list):
        """Esta es una función que nos da como resultado los números negativos de una lista.
        
        -parámetro: list.
        
        -type in list: `int`.
        """
        lista01 = []
        for num in list:
            if num <0:
                lista01.append(num)

        return lista01


lista = (89,-98,50,-48,-20,88,-100,80)
numeros = (2,3,4,8,9)

print(funciones.numerosnegativos(lista))
print(funciones.pares(numeros))
print(funciones.potencia(2,3))
print(funciones.suma_valorespos_yneg(lista))