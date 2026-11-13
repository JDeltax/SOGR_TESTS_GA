import sys

INF = float('inf')

def costo_minimo(x, y, s):
    # dp_c / dp_j = costo mínimo del prefijo si la última letra es C / J
    dp_c = 0 if s[0] != 'J' else INF
    dp_j = 0 if s[0] != 'C' else INF
    for ch in s[1:]:
        nuevo_c = min(dp_c, dp_j + y) if ch != 'J' else INF  # J -> C paga Y
        nuevo_j = min(dp_j, dp_c + x) if ch != 'C' else INF  # C -> J paga X
        dp_c, dp_j = nuevo_c, nuevo_j
    return min(dp_c, dp_j)

lineas = sys.stdin.read().splitlines()
t = int(lineas[0])
for caso in range(1, t + 1):
    x, y, s = lineas[caso].split()
    print(f"Case #{caso}: {costo_minimo(int(x), int(y), s)}")
