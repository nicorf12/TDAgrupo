import time
import random


def leer_archivo(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'r') as archivo:
        next(archivo)  # saltea la linea inicial que indica T_i y B_i
        for linea in archivo:
            elemento1, elemento2 = map(int, linea.strip().split(','))
            datos.append((elemento1, elemento2))
    return datos


def crear_arreglo_con_indice(arr):
    arreglo_con_indice = []
    for indice, valor in enumerate(arr):
        arreglo_con_indice.append([valor, indice])
    return arreglo_con_indice


def minimizar_suma(batallas):
    batallas_indices = crear_arreglo_con_indice(batallas)
    batallas_ordenadas = sorted(batallas_indices, key=lambda batalla: -(batalla[0][1] / batalla[0][0]))
    f = []
    for i in range(len(batallas_ordenadas)):
        if i == 0:
            f.append(batallas_ordenadas[i][0][0])
        else:
            f.append(f[i - 1] + batallas_ordenadas[i][0][0])

    coef_impacto = 0
    for i in range(len(batallas_ordenadas)):
        coef_impacto += f[i] * batallas_ordenadas[i][0][1]

    return coef_impacto, batallas_ordenadas


def generar_batallas_random(tamanio):
    batallas = []
    for i in range(tamanio):
        t = random.randint(1, 1000)
        b = random.randint(0, 1000)
        batallas.append((t, b))
    return batallas


def mostrar_orden_batallas(batallas):
    for i in range(len(batallas)):
        print(
            "Batalla nro: " + str(batallas[i][1]) + ". Tiempo: " + str(batallas[i][0][0]) + ", peso: " + str(
                batallas[i][0][1]))


def obtener_batallas(tamanio):
    batallas = []
    for i in range(tamanio):
        t = int(input("Ingrese el tiempo de la batalla " + str(i) + ": "))
        while t <= 0:
            t = int(input("Ingrese un tiempo valido: "))
        b = int(input("Ingrese el peso de la batalla " + str(i) + ": "))
        while b < 0:
            b = int(input("Ingrese un peso valido: "))
        batallas.append((t, b))
    return batallas


def interaccion_con_senior_fuego():
    print("Bienvenido Señor del fuego, por favor ingrese las batallas que desea ganar el dia de hoy")
    print(
        "En caso de tener unas batallas ya planeadas, por favor ingrese la ruta del archivo en el que la tiene "
        "guardada, para poder calcular de la mejor manera la estrategia")
    respuesta = input("Es este el caso? (S/N): ")
    while respuesta.upper() != "S" and respuesta.upper() != "N":
        respuesta = input("Por favor ingrese S o N: ")
    if respuesta.upper() == "S":
        ruta = input("Ingrese la ruta: ")
        batallas = leer_archivo(ruta)
    else:
        opcion = input("Desea ingresar usted una serie de batallas (1) o desea crear un escenario aleatorio (2)?: ")
        while opcion != "1" and opcion != "2":
            opcion = input("Por favor ingrese una opcion valida: ")
        tamanio = int(input("Ingrese la cantidad de batallas: "))
        if opcion == "1":
            batallas = obtener_batallas(tamanio)
        else:
            batallas = generar_batallas_random(tamanio)
    return batallas


if __name__ == "__main__":
    batallas = interaccion_con_senior_fuego()
    inicio = time.time()
    resultado = minimizar_suma(batallas)
    fin = time.time()
    mostrar_orden_batallas(resultado[1])
    print("COEFICIENTE: ")
    print(resultado[0])
    total = (fin - inicio) * 1000
    print("TIEMPO TOTAL: " + str(total) + " milisegundos")
