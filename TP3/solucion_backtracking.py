import solucion_aproximacion as aprox

def _backtrack(maestros_agua, maestros, grupos, fuerzas, fuerza_actual, mejor_coef, mejor_asignacion, k):
    if len(fuerzas) > 0:
        suma_cuadrados = sum(fuerza**2 for fuerza in fuerzas)
    if len(maestros) == 0:
        if suma_cuadrados <= mejor_coef:
            mejor_coef = suma_cuadrados
            mejor_asignacion = [grupo.copy() for grupo in grupos]
        return mejor_coef, mejor_asignacion

    #si la suma de los cuadrados ya me da mayor al mejor coeficiente conocido, no tiene sentido seguir por esa rama
    if suma_cuadrados >= mejor_coef:
         return mejor_coef, mejor_asignacion

    maestro = maestros.pop()
    for i in range(k):
        grupos[i].append(maestro)
        fuerzas[i] += maestros_agua[maestro]
        mejor_coef, mejor_asignacion = _backtrack(maestros_agua, maestros, grupos, fuerzas, fuerza_actual + maestros_agua[maestro], mejor_coef, mejor_asignacion, k)
        grupos[i].pop()
        fuerzas[i] -= maestros_agua[maestro]
    maestros.append(maestro)

    return mejor_coef, mejor_asignacion


def backtrack(maestros, grupos, fuerzas, fuerza_actual, k):
    if len(maestros) == 0:
        return None, []
    mejor_coef = aprox.aproximacion_tribu_agua(k,maestros)
    mejor_asignacion = []
    maestros_nombres = list(maestros.keys())
    if len(maestros) == k:
        mejor_coef = 0
        grupo_actual = 0
        for maestro in maestros:
            mejor_coef += (maestros[maestro]**2)
            grupos[grupo_actual].append(maestro)
            grupo_actual += 1
            mejor_asignacion = [grupo.copy() for grupo in grupos]
    else:
        mejor_coef, mejor_asignacion = _backtrack(maestros, maestros_nombres, grupos, fuerzas, fuerza_actual, mejor_coef, mejor_asignacion, k)
    return mejor_coef, mejor_asignacion
