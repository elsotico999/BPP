from operator import index
from more_itertools import only
import numpy as np
import pandas as pd
import statistics

df = pd.read_csv('finanzas2020.csv',delimiter=';')
df2 = pd.read_csv('finanzas2020.csv',delimiter=';')
df1 = pd.read_csv('finanzas2020.csv',delimiter=';')
print(df)

print("\n")


df2["Enero"] = pd.to_numeric(df["Enero"], errors='coerce')
df2["Septiembre"] = pd.to_numeric(df["Septiembre"], errors='coerce')
df2["Octubre"] = pd.to_numeric(df["Octubre"], errors='coerce')
df2["Julio"] = pd.to_numeric(df["Julio"], errors='coerce')
df2["Noviembre"] = pd.to_numeric(df["Noviembre"], errors='coerce')


valores_maximos = df2[["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]].max()

print("Los valores máximos de cada columna son:\n",valores_maximos)

print("\n")

valores_minimos = df2[["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]].min()

print("Los valores mínimos de cada columna son:\n",valores_minimos)

print("\n")

df1["Enero"] = df1["Enero"].str.replace('\'','')
df1["Julio"] = df1["Julio"].str.replace('\'','')
df1["Septiembre"] = df1["Septiembre"].str.replace('bug','0')
df1["Octubre"] = df1["Octubre"].str.replace('ups','0')
df1["Noviembre"] = df1["Noviembre"].str.replace('\'','')



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

IngresosEnero,GastosEnero = suma_valorespos_yneg(df1["Enero"])
print("Los ingresos en el mes de Enero han sido", IngresosEnero, "\n"
        "Los gastos en el mes de Enero han sido",-GastosEnero)

IngresosFebrero,GastosFebrero = suma_valorespos_yneg(df1["Febrero"])
print("Los ingresos en el mes de Febrero han sido", IngresosFebrero, "\n"
        "Los gastos en el mes de Febrero han sido",-GastosFebrero)

IngresosMarzo,GastosMarzo = suma_valorespos_yneg(df1["Marzo"])
print("Los ingresos en el mes de Marzo han sido", IngresosMarzo, "\n"
        "Los gastos en el mes de Marzo han sido",-GastosMarzo)

IngresosAbril,GastosAbril = suma_valorespos_yneg(df1["Abril"])
print("Los ingresos en el mes de Abril han sido", IngresosAbril, "\n"
        "Los gastos en el mes de Abril han sido",-GastosAbril)

IngresosMayo,GastosMayo = suma_valorespos_yneg(df1["Mayo"])
print("Los ingresos en el mes de Mayo han sido", IngresosMayo, "\n"
        "Los gastos en el mes de Mayo han sido",-GastosMayo)

IngresosJunio,GastosJunio = suma_valorespos_yneg(df1["Junio"])
print("Los ingresos en el mes de Junio han sido", IngresosJunio, "\n"
        "Los gastos en el mes de Junio han sido",-GastosJunio)

IngresosJulio,GastosJulio = suma_valorespos_yneg(df1["Julio"])
print("Los ingresos en el mes de Julio han sido", IngresosJulio, "\n"
        "Los gastos en el mes de Julio han sido",-GastosJulio)

IngresosAgosto,GastosAgosto = suma_valorespos_yneg(df1["Agosto"])
print("Los ingresos en el mes de Agosto han sido", IngresosAgosto, "\n"
        "Los gastos en el mes de Agosto han sido",-GastosAgosto)

IngresosSeptiembre,GastosSeptiembre = suma_valorespos_yneg(df1["Septiembre"])
print("Los ingresos en el mes de Septiembre han sido", IngresosSeptiembre, "\n"
        "Los gastos en el mes de Septiembre han sido",-GastosSeptiembre)

IngresosOctubre,GastosOctubre = suma_valorespos_yneg(df1["Octubre"])
print("Los ingresos en el mes de Octubre han sido", IngresosOctubre, "\n"
        "Los gastos en el mes de Octubre han sido",-GastosOctubre)

IngresosNoviembre,GastosNoviembre = suma_valorespos_yneg(df1["Noviembre"])
print("Los ingresos en el mes de Noviembre han sido", IngresosNoviembre, "\n"
        "Los gastos en el mes de Noviembre han sido",-GastosNoviembre)

IngresosDiciembre,GastosDiciembre = suma_valorespos_yneg(df1["Diciembre"])
print("Los ingresos en el mes de Diciembre han sido", IngresosDiciembre, "\n"
        "Los gastos en el mes de Diciembre han sido",-GastosDiciembre)

Gastototalaño = -(GastosEnero + GastosFebrero + GastosMarzo + GastosAbril + GastosMayo + GastosJunio + GastosJulio + GastosAgosto + GastosSeptiembre + GastosOctubre + GastosNoviembre + GastosDiciembre) 

Listadegastospormes = [-GastosEnero, -GastosFebrero, -GastosMarzo, -GastosAbril ,-GastosMayo, -GastosJunio, -GastosJulio, -GastosAgosto, -GastosSeptiembre, -GastosOctubre, -GastosNoviembre, -GastosDiciembre]
print("\n")

Ingresostotalaño = IngresosEnero + IngresosFebrero + IngresosMarzo + IngresosAbril + IngresosMayo + IngresosJunio + IngresosJulio + IngresosAgosto + IngresosSeptiembre + IngresosOctubre + IngresosNoviembre + IngresosDiciembre

print("La media de gastos al año es de", statistics.mean(Listadegastospormes))

print("\n")

print("El gasto total a lo largo del año ha sido de", Gastototalaño)

print("\n")

print("Los ingresos totales a lo largo del año han sido de", Ingresostotalaño)

print("\n")


try:
    fichero = open('finanzas2020.csv', 'r')
    lines = fichero.readlines()
    rows = df.columns
    print("Este fichero tiene ", len(rows), "columnas, una para cada mes del año.")
except IOError:
    print("No encuentro el fichero o no puedo leerlo")
else:
     print("He leído el fichero sin problemas, procedo a cerrarlo y a terminar.")
     fichero.close()

print("\n")

try: 
    print("En cada mes hay el siguiente contenido:")
    df.info()
    print("\n")
except IOError:
    print("No se puede especificar o verificar que para cada mes hay contenido.")
else:
    print("Se ha podido verificar correctamente que para cada mes hay contenido.")
