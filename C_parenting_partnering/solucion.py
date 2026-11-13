import sys

datos = sys.stdin.read().split()
pos = 0

def siguiente():
    global pos
    pos += 1
    return int(datos[pos - 1])

t = siguiente()
for caso in range(1, t + 1):
    n = siguiente()
    actividades = [(siguiente(), siguiente(), i) for i in range(n)]
    actividades.sort()  # por hora de inicio

    respuesta = [''] * n
    libre_c = libre_j = 0  # minuto desde el que cada uno queda libre
    posible = True
    for inicio, fin, i in actividades:
        if libre_c <= inicio:
            respuesta[i] = 'C'
            libre_c = fin
        elif libre_j <= inicio:
            respuesta[i] = 'J'
            libre_j = fin
        else:
            posible = False
            break

    print(f"Case #{caso}: {''.join(respuesta) if posible else 'IMPOSSIBLE'}")
