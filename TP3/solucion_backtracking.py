def _backtrack(maestros, grupos, fuerzas, fuerza_actual, mejor_coef, mejor_asignacion):
        if len(maestros) == 0:
            suma_cuadrados = sum(fuerza**2 for fuerza in fuerzas)
            if mejor_coef is None or suma_cuadrados < mejor_coef:
                mejor_coef = suma_cuadrados
                mejor_asignacion = [grupo.copy() for grupo in grupos]
            return mejor_coef, mejor_asignacion

        maestro = maestros.pop()
        for i in range(k):
            grupos[i].append(maestro)
            fuerzas[i] += maestros_agua[maestro]
            mejor_coef, mejor_asignacion = _backtrack(maestros, grupos, fuerzas, fuerza_actual + maestros_agua[maestro], mejor_coef, mejor_asignacion)
            grupos[i].pop()
            fuerzas[i] -= maestros_agua[maestro]
        maestros.append(maestro)

        return mejor_coef, mejor_asignacion

def backtrack(maestros, grupos, fuerzas, fuerza_actual):
    mejor_coef = None
    mejor_asignacion = []
    mejor_coef, mejor_asignacion = _backtrack(maestros, grupos, fuerzas, fuerza_actual, mejor_coef, mejor_asignacion)
    return mejor_coef, mejor_asignacion

# Hacer que sea desde archivo!! dejo un ejemplo :D

maestros_agua = {
    'Unalaq': 358,
    'Misu': 701,
    'Hama': 712,
    'Hasook': 640,
    'Tonraq': 10,
    'Amon': 37,
    'Katara': 828,
    'Rafa': 291
}

k = 3  
grupos_iniciales = [[] for _ in range(k)]
fuerzas_iniciales = [0] * k
maestros = list(maestros_agua.keys())

coef, mejor_asignacion = backtrack(maestros, grupos_iniciales, fuerzas_iniciales, 0)

for i, grupo in enumerate(mejor_asignacion, 1):
    print(f"Grupo {i}: {', '.join(grupo)}")

print("Coeficiente:", coef)
