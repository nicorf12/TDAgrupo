import solucion_backtracking
def main(archivo):
    maestros = []
    habilidades = []
    with open(archivo, "r") as archivo:
        grupos = int(archivo.readline().strip())
        nombre, valor = map(str, archivo.readline().strip().split(','))
        maestro, habilidad = nombre,int(valor)
        maestros.append(maestro)
        habilidades.append(habilidad)
    #backtracking:
    coef, mejor_asignacion = solucion_backtracking.backtrack(maestros, [[] for _ in range(grupos)], [0]*grupos, 0)

    for i, grupo in enumerate(mejor_asignacion, 1):
        print(f"Grupo {i}: {', '.join(grupo)}")
    print("Coeficiente:", coef)

    #PL:


if __name__ == "__main__":
    main("archivos/6_3.txt")