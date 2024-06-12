def aproximacion_tribu_agua(k, habilidades):
    maestros_ordenados = sorted(habilidades.values(), reverse=True)
    grupos = [[] for _ in range(k)]
    
    for maestro in maestros_ordenados:
        grupo_minimo = min(grupos, key=lambda x: sum(x))
        grupo_minimo.append(maestro)
    
    suma_cuadrados_total = sum(sum(grupo) ** 2 for grupo in grupos)
    
    return suma_cuadrados_total

# O(n*logn + n*k)