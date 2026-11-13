import sys

# Leemos todos los números como tokens: así no importa cómo vengan partidas las líneas
datos = sys.stdin.read().split()
pos = 0

def siguiente():
    global pos
    pos += 1
    return int(datos[pos - 1])

t = siguiente()
for caso in range(1, t + 1):
    n = siguiente()
    dados = sorted(siguiente() for _ in range(n))  # orden numérico, no de texto
    largo = 0
    for caras in dados:
        # si este dado alcanza a mostrar el siguiente escalón, lo usamos
        if caras > largo:
            largo += 1
    print(f"Case #{caso}: {largo}")
