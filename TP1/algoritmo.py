import time


def leer_archivo(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'r') as archivo:
        next(archivo) #saltea la linea inicial que indica T_i y B_i
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
    batallas_ordenadas = sorted(batallas_indices , key=lambda batalla: -(batalla[0][1]/batalla[0][0]))
    f = []
    for i in range(len(batallas_ordenadas)):
        if i == 0:
            f.append(batallas_ordenadas[i][0][0])
        else:
            f.append(f[i - 1] + batallas_ordenadas[i][0][0])

    coef_impacto = 0
    for i in range(len(batallas_ordenadas)):
        coef_impacto += f[i] * batallas_ordenadas[i][0][1]

    for i in range(len(batallas_ordenadas)):
        print(
            "Batalla nro: " + str(batallas_ordenadas[i][1]) + ". Tiempo: " + str(batallas_ordenadas[i][0][0]) + ", peso: " + str(
                batallas_ordenadas[i][0][1]))

    return coef_impacto


if __name__ == "__main__":
    inicio = time.time()
    coef = minimizar_suma(leer_archivo("archivos/100000.txt"))
    print("COEFICIENTE: ")
    print(coef)
    fin = time.time()
    total = (fin-inicio)*1000
    print("TIEMPO TOTAL: " + str(total) + " milisegundos")