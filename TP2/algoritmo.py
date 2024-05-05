import sys
import random

def generar_datos_aleatorios(n, f_cste,soldados_cste):
    f = [random.randint(1, n)]
    for _ in range(n-1):
        f_anterior = f[-1]
        if f_cste:nueva_f = f_anterior 
        else:nueva_f = f_anterior + random.randint(0, 5)
        f.append(nueva_f)

    if soldados_cste: rafagas = [random.randint(10,200)]*(n)
    else: rafagas = [random.randint(0,f[-1]) for _ in range(n)]

    
    return rafagas, n, f

def crear_archivo_datos_aleatorios(n):
    rafagas,_,f = generar_datos_aleatorios(n,False,False)

    with open(f"./sets/{n}.txt", 'w') as archivo:
        archivo.write(f"#{n} rafagas\n")
        archivo.write(f"{n}\n")
        for soldados in rafagas:
            archivo.write(f"{soldados}\n")
        for energia in f:
            archivo.write(f"{energia}\n")

    print(f"Archivo {n} creado con éxito.")

def cargasOptimasDinamica(rafagas:list[int], j:int, f:list[int]):
    rafagas.insert(0,0)
    f.insert(0,0)
    posibilidad = []
    for _ in range(j+1):
        posibilidad.append([0]*(j+1))
    maxs = [0]*(j+1)

    for k in range(1,len(posibilidad)):
        for j in range(1,k+1):
            posibilidad[k][j] =  posibilidad[k-j][maxs[k-j]] + min(rafagas[k] , f[j])
        maxs[k] = posibilidad[k].index(max(posibilidad[k]))

    valor_max = posibilidad[len(posibilidad)-1][maxs[len(posibilidad)-1]]
    
    ataques = []
    k = len(posibilidad)-1
    while k > 0:
        ataques.append(k)
        k = k-maxs[k]

    solucion = ""
    for i in range(1,j+1):
        if i in ataques:
            solucion+="ATACAR, "
        else:
            solucion+="CARGAR, "

    return solucion[:-2],valor_max


def main(archivo):
    with open(archivo,"r") as archivo:
        next(archivo)
        j =  int(archivo.readline().strip())
        rafagas = [int(archivo.readline().strip()) for _ in range(j)]
        f = [int(archivo.readline().strip()) for _ in range(j)]

    orden_ataques, tropa_eliminadas=cargasOptimasDinamica(rafagas,j,f)
    print(f"Estrategia: {orden_ataques}.\nCantidad de tropas eliminadas: {tropa_eliminadas}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python algoritmo.py <archivo>")
    else:
        filename = sys.argv[1]
        main(filename)