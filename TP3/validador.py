def validador(n, k, B, S, habilidades):
    if len(habilidades) != n: return False

    suma = 0
    for s in S:
        suma += len(s)
    if suma != n: return False #si la suma de todos los elementos de cada conjunto no me da la cantidad original esta mal

    suma = 0
    for conjunto in S:
        suma_actual = 0
        for elemento in conjunto:
            suma_actual += elemento
        suma += suma_actual**2

    return suma <= B
