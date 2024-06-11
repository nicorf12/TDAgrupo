def _backtrack(maestros_agua, maestros, grupos, fuerzas, fuerza_actual, mejor_coef, mejor_asignacion, k):
    if len(fuerzas) > 0:
        suma_cuadrados = sum(fuerza**2 for fuerza in fuerzas)
    if len(maestros) == 0:
        if mejor_coef is None or suma_cuadrados < mejor_coef:
            mejor_coef = suma_cuadrados
            mejor_asignacion = [grupo.copy() for grupo in grupos]
        return mejor_coef, mejor_asignacion

    if mejor_coef is not None and suma_cuadrados >= mejor_coef:
        return mejor_coef, mejor_asignacion

    maestro = maestros.pop()
    for i in range(k):
        if mejor_coef is None or fuerzas[i] + maestros_agua[maestro] < mejor_coef:
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
    mejor_coef = None
    mejor_asignacion = []
    maestros_nombres = list(maestros.keys())
    if len(maestros) == k:
        mejor_coef = 0
        for maestro in maestros:
            mejor_coef += (maestros[maestro]**2)
            mejor_asignacion.append(maestro)
    else:
        mejor_coef, mejor_asignacion = _backtrack(maestros, maestros_nombres, grupos, fuerzas, fuerza_actual, mejor_coef, mejor_asignacion, k)
    return mejor_coef, mejor_asignacion
