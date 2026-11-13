import sys

def diversion_total(f, p):
    n = len(f)
    hijos = [[] for _ in range(n + 1)]  # el 0 es el abismo
    for i in range(1, n + 1):
        hijos[p[i - 1]].append(i)

    # lleva[i] = el mayor F que sube por i en la cadena que lo activa
    lleva = [0] * (n + 1)
    total = 0
    # como P[i] < i, recorrer de n hacia 1 procesa los hijos antes que el padre
    for i in range(n, 0, -1):
        if not hijos[i]:
            lleva[i] = f[i - 1]
            continue
        valores = [lleva[h] for h in hijos[i]]
        menor = min(valores)
        # solo la cadena con el menor valor sigue subiendo; las demás se cobran aquí
        total += sum(valores) - menor
        lleva[i] = max(f[i - 1], menor)

    return total + sum(lleva[h] for h in hijos[0])

datos = sys.stdin.read().split()
pos = 0
def siguiente():
    global pos
    pos += 1
    return int(datos[pos - 1])

t = siguiente()
for caso in range(1, t + 1):
    n = siguiente()
    f = [siguiente() for _ in range(n)]
    p = [siguiente() for _ in range(n)]
    print(f"Case #{caso}: {diversion_total(f, p)}")
