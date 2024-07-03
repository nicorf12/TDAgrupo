import heapq

def aproximacion_tribu_agua(k, habilidades):
    maestros_ordenados = sorted(habilidades.values(), reverse=True)

    heap = [(0, i) for i in range(k)]
    heapq.heapify(heap)
    
    grupos = [[] for _ in range(k)]
    
    for maestro in maestros_ordenados:
        suma_actual, grupo_index = heapq.heappop(heap)
        grupos[grupo_index].append(maestro)
        nueva_suma = suma_actual + maestro
        heapq.heappush(heap, (nueva_suma, grupo_index))
    
    suma_cuadrados_total = sum(sum(grupo) ** 2 for grupo in grupos)
    
    return suma_cuadrados_total

