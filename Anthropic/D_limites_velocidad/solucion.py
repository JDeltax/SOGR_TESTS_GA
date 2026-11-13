import sys

class Cubeta:
    def __init__(self, capacidad, recarga):
        self.capacidad = capacidad
        self.recarga = recarga      # tokens por segundo
        self.tokens = capacidad     # empieza llena
        self.ultimo = 0

    def actualizar(self, t):
        # se recarga sin parar, pero nunca pasa de la capacidad
        self.tokens = min(self.capacidad, self.tokens + self.recarga * (t - self.ultimo))
        self.ultimo = t

    def espera(self, necesito):
        # segundos enteros (hacia arriba) hasta tener lo que necesito
        if self.tokens >= necesito:
            return 0
        falta = necesito - self.tokens
        return -(-falta // self.recarga)

solicitudes = Cubeta(3, 1)
tokens_entrada = Cubeta(100, 20)

for linea in sys.stdin.read().splitlines():
    partes = linea.split()
    if not partes:
        continue
    t, nuevos = int(partes[1]), int(partes[2])
    # partes[3] son los tokens leídos de caché: no cuentan para el límite

    solicitudes.actualizar(t)
    tokens_entrada.actualizar(t)

    if solicitudes.tokens >= 1 and tokens_entrada.tokens >= nuevos:
        solicitudes.tokens -= 1
        tokens_entrada.tokens -= nuevos
        print("ok")
    else:
        espera = max(solicitudes.espera(1), tokens_entrada.espera(nuevos))
        print(f"429 retry-after={espera}")
