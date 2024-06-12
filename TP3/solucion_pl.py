import pulp

def balancear_grupos_minima_diferencia(maestros, k):
    n = len(maestros)
    x = list(maestros.values())
    nombres = list(maestros.keys())

    prob = pulp.LpProblem("BalancearGrupos_MinimaDiferencia", pulp.LpMinimize)

    # ---------------- Variables ------------------
    x_ij = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(k)), cat='Binary')
    S_j = pulp.LpVariable.dicts("S", (j for j in range(k)), lowBound=0, cat='Continuous')
    Z = pulp.LpVariable("Z", lowBound=0, cat='Continuous')
    Y = pulp.LpVariable("Y", lowBound=0, cat='Continuous')

    #---------------- Funcion Objetivo ---------------
    prob += Z - Y
    #---------------- Restricciones ---------------
    # cada maestro en exactamente un grupo
    for i in range(n):
        prob += sum(x_ij[i, j] for j in range(k)) == 1

    # definicion de las sumas de fuerzas de los grupos
    for j in range(k):
        prob += S_j[j] == sum(x[i] * x_ij[i, j] for i in range(n))

    # definicion de Z y Y
    for j in range(k):
        prob += Z >= S_j[j]
        prob += Y <= S_j[j]

    solver = pulp.PULP_CBC_CMD(msg=False)
    prob.solve(solver)

    sum_of_squares = 0
    mejor_asignacion = []
    for j in range(k):
        mejor_asignacion.append([])
        group_sum = sum(x[i] for i in range(n) if pulp.value(x_ij[i, j]) == 1)
        sum_of_squares += group_sum**2
        for i in range(n):
            if pulp.value(x_ij[i, j]) == 1:
                mejor_asignacion[j].append(nombres[i])

    return sum_of_squares, mejor_asignacion



def balancear_grupos_mininima_desviacion(maestros, k):
    n = len(maestros)
    x = list(maestros.values())
    nombres = list(maestros.keys())

    prob = pulp.LpProblem("BalancearGrupos_MininimaDesviacion", pulp.LpMinimize)

    # ---------------- Variables ------------------
    x_ij = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(k)), cat='Binary')
    S_j = pulp.LpVariable.dicts("S", (j for j in range(k)), lowBound=0, cat='Continuous')
    T = pulp.LpVariable("T", lowBound=0, cat='Continuous')
    D_j = pulp.LpVariable.dicts("D", (j for j in range(k)), lowBound=0, cat='Continuous')

    #---------------- Funcion Objetivo ---------------
    prob += pulp.lpSum(D_j[j] for j in range(k))
    #---------------- Restricciones ---------------
    # cada maestro en exactamente un grupo
    for i in range(n):
        prob += sum(x_ij[i, j] for j in range(k)) == 1

    # definicion de las sumas de fuerzas de los grupos
    for j in range(k):
        prob += S_j[j] == sum(x[i] * x_ij[i, j] for i in range(n))

    # definición de las desviaciones respecto a la variable objetivo
    for j in range(k):
        prob += D_j[j] >= S_j[j] - T
        prob += D_j[j] >= T - S_j[j]

    solver = pulp.PULP_CBC_CMD(msg=False)
    prob.solve(solver)

    sum_of_squares = 0

    mejor_asignacion = []
    for j in range(k):
        mejor_asignacion.append([])
        group_sum = sum(x[i] for i in range(n) if pulp.value(x_ij[i, j]) == 1)
        sum_of_squares += group_sum**2
        for i in range(n):
            if pulp.value(x_ij[i, j]) == 1:
                mejor_asignacion[j].append(nombres[i])

    return sum_of_squares, mejor_asignacion