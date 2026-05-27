# =========================================================
# PROGRAMA: Clasificación de compromiso de sesiones
# =========================================================

# -----------------------------
# MATRIZ DE DATOS INICIALES
# -----------------------------
# Cada fila contiene:
# [ID Cliente, Duración en segundos, Número de clics]

sesiones = [
    ["C001", 250, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 70, 1]
]


# -------------------------------------------------
# FUNCIÓN PARA CLASIFICAR EL NIVEL DE COMPROMISO
# -------------------------------------------------
def clasificar_compromiso(duracion, clics):

    # Condición para compromiso ALTO
    if duracion > 180 and clics > 8:
        return "Alto"

    # Condición para compromiso BAJO
    elif duracion < 60 or clics < 3:
        return "Bajo"

    # Todos los demás casos
    else:
        return "Medio"


# --------------------------------------
# GENERACIÓN DEL INFORME FINAL
# --------------------------------------
print("===== INFORME DE COMPROMISO =====\n")

# Recorremos cada fila de la matriz
for sesion in sesiones:

    # Extraemos los datos de la fila
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    # Llamamos la función de clasificación
    clasificacion = clasificar_compromiso(duracion, clics)

    # Mostramos el resultado
    print(f"Cliente: {id_cliente} -> Compromiso: {clasificacion}")