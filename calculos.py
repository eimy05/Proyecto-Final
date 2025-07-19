def obtener_resultados(posiciones, fuerzas):
    x_vals = []
    V_vals = []
    for i in range(len(posiciones)):
        x_vals.append(posiciones[i])
        V_vals.append(sum(fuerzas[:i+1]))
        if i < len(posiciones) - 1:
            x_vals.append(posiciones[i+1])
            V_vals.append(sum(fuerzas[:i+1]))

    # Calcular momentos con método de áreas
    M_vals = [0]
    for i in range(1, len(x_vals)):
        base = x_vals[i] - x_vals[i-1]
        altura1 = V_vals[i-1]
        altura2 = V_vals[i]
        area = (altura1 + altura2) / 2 * base
        M_vals.append(M_vals[-1] + area)

    return x_vals, V_vals, M_vals
