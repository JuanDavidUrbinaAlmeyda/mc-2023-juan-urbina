def gauss_jordan_inversa(A):
    n = len(A)
    
    # Crear la matriz extendida
    A_ext = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(A[i][j])
        for j in range(n):
            if j == i:
                fila.append(1)
            else:
                fila.append(0)
        A_ext.append(fila)

    # Eliminación gaussiana
    for i in range(n):
        # Pivoteo parcial por columnas
        max_fila = i + max(range(n-i), key=lambda x: abs(A_ext[x][i]))
        A_ext[i], A_ext[max_fila] = A_ext[max_fila], A_ext[i]

        # División por el pivote
        pivote = A_ext[i][i]
        for j in range(i, 2*n):
            A_ext[i][j] /= pivote

        # Eliminación hacia adelante y hacia atrás
        for k in range(n):
            if k != i:
                factor = A_ext[k][i]
                for j in range(i, 2*n):
                    A_ext[k][j] -= factor * A_ext[i][j]

    # Extraer la matriz inversa
    A_inv = []
    for i in range(n):
        fila = []
        for j in range(n, 2*n):
            fila.append(A_ext[i][j])
        A_inv.append(fila)

    return A_inv

# Ejemplo de uso
A = [[3, 2, 2],
     [3, 1, -3],
     [1, 0, -2]]
A_inv = gauss_jordan_inversa(A)
print(A_inv)
B = [[1, 2, 0, 4],
     [2, 0, -1, -2],
     [1, 1, -1, 0],
     [0, 4, 1, 0]]
B_inv= gauss_jordan_inversa(B)
print(B_inv)