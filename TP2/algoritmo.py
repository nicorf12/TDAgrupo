import sys

def algoritmo(rafagas:list[int], j:int, f:list[int]):
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
        rafagas.insert(0,0)
        f = [int(archivo.readline().strip()) for _ in range(j)]
        f.insert(0,0)

    orden_ataques, tropa_eliminadas=algoritmo(rafagas,j,f)
    print(f"Estrategia: {orden_ataques}.\nCantidad de tropas eliminadas: {tropa_eliminadas}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python algoritmo.py <archivo>")
    else:
        filename = sys.argv[1]
        main(filename)