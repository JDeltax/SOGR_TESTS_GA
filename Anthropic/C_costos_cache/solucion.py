import sys
import json

# Todo en millonésimas de dólar (micro-dólares) y con enteros.
# $3 por millón de tokens = 3 micro-dólares por token; $15 por millón = 15.
# Para no usar 1.25 y 0.1 multiplico todo por 100 y divido al final:
#   entrada 300, escritura en caché 375 (1.25x), lectura de caché 30 (0.1x), salida 1500
def costo_x100(u):
    return (u['input_tokens'] * 300
            + u['cache_creation_input_tokens'] * 375
            + u['cache_read_input_tokens'] * 30
            + u['output_tokens'] * 1500)

def sin_cache_x100(u):
    entrada = u['input_tokens'] + u['cache_creation_input_tokens'] + u['cache_read_input_tokens']
    return entrada * 300 + u['output_tokens'] * 1500

def dolares(micro):
    return f"${micro // 1_000_000}.{micro % 1_000_000:06d}"

total = sin_cache = 0
aciertos = n = 0
for linea in sys.stdin.read().splitlines():
    if not linea.strip():
        continue
    u = json.loads(linea)
    n += 1
    costo = costo_x100(u) // 100
    total += costo
    sin_cache += sin_cache_x100(u) // 100
    if u['cache_read_input_tokens'] > 0:
        aciertos += 1
    print(f"solicitud {n}: {dolares(costo)}")

print(f"total: {dolares(total)}")
print(f"sin_cache: {dolares(sin_cache)}")
print(f"ahorro: {dolares(sin_cache - total)}")
print(f"aciertos_de_cache: {aciertos}/{n}")
