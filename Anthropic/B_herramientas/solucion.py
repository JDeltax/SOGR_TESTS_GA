import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

CLIMA = {'Bogotá': 14, 'Medellín': 24, 'Cali': 26}

def calculadora(entrada):
    op, a, b = entrada['operacion'], entrada['a'], entrada['b']
    if op == 'sumar':
        return str(a + b)
    if op == 'restar':
        return str(a - b)
    if op == 'multiplicar':
        return str(a * b)
    if op == 'dividir':
        if b == 0:
            return 'error: división por cero'
        # // en Python redondea hacia abajo (-7 // 2 = -4); la división entera de verdad trunca hacia cero
        return str(abs(a) // abs(b) * (1 if (a < 0) == (b < 0) else -1))
    return f'error: operación desconocida: {op}'

def clima(entrada):
    ciudad = entrada['ciudad']
    if ciudad in CLIMA:
        return f'{CLIMA[ciudad]} °C'
    return f'error: ciudad desconocida: {ciudad}'

HERRAMIENTAS = {'calculadora': calculadora, 'clima': clima}

llamadas = errores = 0
for linea in sys.stdin.read().splitlines():
    if not linea.strip():
        continue
    respuesta = json.loads(linea)
    if respuesta['stop_reason'] == 'tool_use':
        for bloque in respuesta['content']:
            if bloque['type'] != 'tool_use':
                continue
            funcion = HERRAMIENTAS.get(bloque['name'])
            if funcion:
                resultado = funcion(bloque['input'])
            else:
                resultado = f"error: herramienta desconocida: {bloque['name']}"
            llamadas += 1
            if resultado.startswith('error:'):
                errores += 1
            print(f"tool_result {bloque['id']} {resultado}")
    elif respuesta['stop_reason'] == 'end_turn':
        texto = ''.join(b['text'] for b in respuesta['content'] if b['type'] == 'text')
        print(f"final: {texto}")

print(f"resumen: {llamadas} llamadas, {errores} errores")
