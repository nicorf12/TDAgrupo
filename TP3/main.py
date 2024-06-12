import sys
import time
import solucion_backtracking
import solucion_pl
import solucion_aproximacion as aprox

def main(archivo, resolucion):
    maestros_agua = {}
    with open(archivo, "r") as archivo:
        grupos = int(archivo.readline().strip())
        for linea in archivo:
            nombre, valor = map(str, linea.strip().split(','))
            maestro, habilidad = nombre,int(valor)
            maestros_agua[maestro] = habilidad

    if resolucion == 'b':
        coef, mejor_asignacion = solucion_backtracking.backtrack(maestros_agua, [[] for _ in range(grupos)], [0]*grupos, 0, grupos)
        for i, grupo in enumerate(mejor_asignacion, 1):
            print(f"Grupo {i}: {', '.join(grupo)}")
        print("Coeficiente:", coef)
    elif resolucion == 'pl':
        coef, mejor_asignacion = solucion_pl.balancear_grupos_mininima_desviacion(maestros_agua,grupos)
        for i, grupo in enumerate(mejor_asignacion, 1):
            print(f"Grupo {i}: {', '.join(grupo)}")
        print("Coeficiente:", coef)
    elif resolucion == "aprox":
        coef = aprox.aproximacion_tribu_agua(grupos, maestros_agua)
        print(coef)

def mostrar_tiempo(inicio, fin):
    total = fin - inicio
    segundos = 0
    minutos = 0
    horas = 0
    if total > 60 and total < 3600:
        minutos = total // 60
        segundos = total % 60
        segundos //= 1
    elif total > 3600:
        minutos = total % 60;
        horas = total // 3600
    else:
        if total < 1: segundos = total
        else: segundos = total // 1

    if horas >= 1: print(horas, " horas")
    if minutos >= 1: print(minutos, " minutos")
    print(segundos, " segundos")
    return

if __name__ == "__main__":
    inicio = time.time()
    if len(sys.argv) != 3:
        print("Uso: python algoritmo.py <archivo> <b/pl>")
    else:
        if sys.argv[2] != 'b' and sys.argv[2] != 'pl' and sys.argv[2] != 'aprox':
            print("Ingrese una opcion valida de resolucion")
        else:
            filename = sys.argv[1]
            resolucion = sys.argv[2]
            main(filename, resolucion)
    fin = time.time()
    mostrar_tiempo(inicio, fin)