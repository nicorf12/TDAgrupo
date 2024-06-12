import random
import string
import pandas as pd
import numpy as np
import timeit
import time
import matplotlib.pyplot as plt
import solucion_pl as pl
import solucion_backtracking as bt
import os
import glob

def generar_nombre_aleatorio():
    return ''.join(random.choices(string.ascii_letters, k=5))

def generar_maestros_aleatorios(cantidad):
    maestros = {}
    for _ in range(cantidad):
        nombre = generar_nombre_aleatorio()
        habilidad = random.randint(1, 1000)
        maestros[nombre] = habilidad
    return maestros

def asignar_valores(k):
    cantidad_maestros = random.randint(k, 2 * k)
    maestros = generar_maestros_aleatorios(cantidad_maestros)
    return maestros,k

def generar_archivo(nombre_archivo):
    maestros, k = asignar_valores()
    with open(nombre_archivo, 'w') as file:
        file.write(f"{k}\n")
        for nombre in maestros:
            file.write(f"{nombre}, {maestros[nombre]}\n")

def crear_sets():
    for i in range(5):
        generar_archivo(f"sets/set_{i}.txt")

def generar_grafico_complejidad_teorica(solucion):
    rango = range(10)

    tiempos = []
    if solucion == "pl":  
        for r in rango:
            tiempos.append(timeit.timeit(lambda: pl.balancear_grupos_minima_diferencia(*asignar_valores(r)), globals=globals(), number=2))
    elif solucion == "bk":
        for r in rango:
            tiempos.append(timeit.timeit(lambda: bt.backtrack(*asignar_valores(r)), globals=globals(), number=1))

    x = np.array(rango)
    y = np.array(tiempos)

    a, b = ajustar_modelo_exponencial(x, y)

    plt.plot(x, y, 'r', label='Datos originales', markersize=8, color='blue')
    plt.plot(x, a * np.exp(b * x), label='Ajuste exponencial', color='green', linestyle='--', linewidth=2)
    plt.title('Ajuste de Complejidad Teórica (2^n) vs Tiempos de Ejecución')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend(loc='best')
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.ylim([0, max(y) * 1.1])
    plt.xlim([0, max(x) * 1.1])
    plt.show()

def ajustar_modelo_exponencial(x, y):
    y_log = np.log(y)
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y_log, rcond=None)[0]
    return np.exp(c), m

def generar_grafico_PL_BT():
    rango = range(5)
    
    tiempos_pl = []
    for r in rango:
        tiempos_pl.append(timeit.timeit(lambda: pl.balancear_grupos_minima_diferencia(*asignar_valores(r)), globals=globals(), number=1))

    tiempos_bt = []
    for r in rango:
        tiempos_bt.append(timeit.timeit(lambda: bt.backtrack(*asignar_valores(r)), globals=globals(), number=1))

    plt.plot(rango, tiempos_pl, 'r', label='Programacion Lineal')
    plt.plot(rango, tiempos_bt, 'r', label='Backtraking')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.show()

def vs_pl():
    carpeta = './sets'
    archivos = glob.glob(os.path.join(carpeta, '*'))

    cadena = ""
    for archivo in archivos:
        inicio = time.time()
        coef, mejor_asignacion = pl.balancear_grupos_mininima_desviacion(archivo)
        fin = time.time()
        cadena+= f"-> {archivo} por minima desviacion\n"
        for i, grupo in enumerate(mejor_asignacion, 1):
            cadena+=f"Grupo {i}: {', '.join(grupo)}\n"
        cadena += f"Coeficiente:, {coef}\n {archivo} - tardo {fin - inicio}, segundos.\n\n"

        inicio = time.time()
        coef, mejor_asignacion = pl.balancear_grupos_minima_diferencia(archivo)
        fin = time.time()

        cadena+= f"-> {archivo} por minima diferencia\n"
        for i, grupo in enumerate(mejor_asignacion, 1):
            cadena+=f"Grupo {i}: {', '.join(grupo)}\n"
        cadena += f"Coeficiente:, {coef}\n {archivo} - tardo {fin - inicio}, segundos.\n\n"
    
    with open("sets/VS_PL", 'w') as archivo:
        archivo.write(cadena)

generar_grafico_complejidad_teorica("pl")