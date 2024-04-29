import sys
import random

def generar_datos_aleatorios(n, f_cste,soldados_cste):
    f = [random.randint(1, n)]
    for _ in range(n-1):
        f_anterior = f[-1]
        if f_cste:nueva_f = f_anterior
        else:nueva_f = random.randint(f_anterior, f_anterior + f_anterior//2)
        f.append(nueva_f)

    if soldados_cste: rafagas = [random.randint(10, 200)]*n
    else: rafagas = [random.randint(10, 200) for _ in range(n)]

    rafagas.insert(0,0)
    f.insert(0,0)
    return rafagas, n, f

def crear_archivo_datos_aleatorios(n):
    rafagas,_,f = generar_datos_aleatorios(n)

    with open(f"{n}.txt", 'w') as archivo:
        archivo.write(f"#{n} batallas\n")
        for soldados in rafagas:
            archivo.write(f"{soldados}\n")
        for energia in f:
            archivo.write(f"{energia}\n")

    print(f"Archivo {n} creado con éxito.")

def reconstruir_solucion(posibilidad, maxs, j):
    ataques = []
    k = len(posibilidad) - 1
    while k > 0:
        ataques.insert(0,k)
        k = k - maxs[k]

    solucion = []
    for i in range(1, j + 1):
        if i in ataques:
            solucion.append("ATACAR")
        else:
            solucion.append("CARGAR")
    return solucion

def cargasOptimasDinamica(rafagas:list[int], j:int, f:list[int]):
    posibilidad = []
    for _ in range(j+1):
        posibilidad.append([0]*(j+1))
    maxs = [0]*(j+1)

    for k in range(1,len(posibilidad)):
        for j in range(1,k+1):
            posibilidad[k][j] =  posibilidad[k-j][maxs[k-j]] + min(rafagas[k] , f[j])
        maxs[k] = posibilidad[k].index(max(posibilidad[k]))

    valor_max = posibilidad[len(posibilidad)-1][maxs[len(posibilidad)-1]]
    return reconstruir_solucion(posibilidad, maxs, j), valor_max


def main(archivo):
    with open(archivo,"r") as archivo:
        next(archivo)
        j =  int(archivo.readline().strip())
        rafagas = [int(archivo.readline().strip()) for _ in range(j)]
        rafagas.insert(0,0)
        f = [int(archivo.readline().strip()) for _ in range(j)]
        f.insert(0,0)

    orden_ataques, tropa_eliminadas=cargasOptimasDinamica(rafagas,j,f)
    print(f"Estrategia: {orden_ataques}.\nCantidad de tropas eliminadas: {tropa_eliminadas}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python algoritmo.py <archivo>")
    else:
        filename = sys.argv[1]
        main(filename)