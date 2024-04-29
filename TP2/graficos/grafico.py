import pandas as pd
import numpy as np
import timeit
import matplotlib.pyplot as plt

from TP2.algoritmo import cargasOptimasDinamica,generar_datos_aleatorios

plt.rc('font', size=15)
CANTIDADES_A_PROBAR = range(10, 2001, 200)
CANT_EXPERIMENTOS = 10

def armarGrafico_ComparacionDeComplejidad():
    tiempos = []

    for cant in CANTIDADES_A_PROBAR: 
        tiempos.append(timeit.timeit(lambda: cargasOptimasDinamica(*generar_datos_aleatorios(cant,False,False)), globals=globals(), number=CANT_EXPERIMENTOS))

    df = pd.DataFrame()
    df['i'] = CANTIDADES_A_PROBAR
    df['Cargas Optimas'] = tiempos

    coeficiente_x_cuadrado = np.power(df['i'].iloc[1], 2) / tiempos[1]
    df['x^2'] = np.power(df['i'], 2) / coeficiente_x_cuadrado

    ax = df.plot(x='i', figsize=(10, 5))
    ax.set_xlabel("CANTIDAD DE ELEMENTOS")
    ax.set_ylabel("SEGUNDOS")
    plt.show()

def armarGrafico_Fcste():
    tiempos = []

    for cant in CANTIDADES_A_PROBAR: 
        tiempos.append(timeit.timeit(lambda: cargasOptimasDinamica(*generar_datos_aleatorios(cant,True,False)), globals=globals(), number=CANT_EXPERIMENTOS))

    df = pd.DataFrame()
    df['i'] = CANTIDADES_A_PROBAR
    df['Cargas Optimas'] = tiempos

    coeficiente_x_cuadrado = np.power(df['i'].iloc[1], 2) / tiempos[1]
    df['x^2'] = np.power(df['i'], 2) / coeficiente_x_cuadrado

    ax = df.plot(x='i', figsize=(10, 5))
    ax.set_xlabel("CANTIDAD DE ELEMENTOS")
    ax.set_ylabel("SEGUNDOS")
    plt.show()

def armarGrafico_Soldadoscste():
    tiempos = []

    for cant in CANTIDADES_A_PROBAR: 
        tiempos.append(timeit.timeit(lambda: cargasOptimasDinamica(*generar_datos_aleatorios(cant,False,True)), globals=globals(), number=CANT_EXPERIMENTOS))

    df = pd.DataFrame()
    df['i'] = CANTIDADES_A_PROBAR
    df['Cargas Optimas'] = tiempos

    coeficiente_x_cuadrado = np.power(df['i'].iloc[1], 2) / tiempos[1]
    df['x^2'] = np.power(df['i'], 2) / coeficiente_x_cuadrado

    ax = df.plot(x='i', figsize=(10, 5))
    ax.set_xlabel("CANTIDAD DE ELEMENTOS")
    ax.set_ylabel("SEGUNDOS")
    plt.show()

def main():
    armarGrafico_ComparacionDeComplejidad()
    #algoritmo.crear_archivo_datos_aleatorios(50)
    #armarGrafico_Fcste()
    #armarGrafico_Soldadoscste()
main()