import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

bloques = {}
stop_reason = None
input_tokens = output_tokens = 0

for linea in sys.stdin.read().splitlines():
    # la línea "event:" repite el tipo que ya viene dentro del JSON, así que basta con "data:"
    if not linea.startswith('data:'):
        continue
    evento = json.loads(linea[len('data:'):])
    tipo = evento['type']

    if tipo == 'message_start':
        bloques = {}
        stop_reason = None
        input_tokens = evento['message']['usage']['input_tokens']
    elif tipo == 'content_block_delta' and evento['delta']['type'] == 'text_delta':
        i = evento['index']
        bloques[i] = bloques.get(i, '') + evento['delta']['text']
    elif tipo == 'message_delta':
        stop_reason = evento['delta']['stop_reason']
        output_tokens = evento['usage']['output_tokens']
    elif tipo == 'message_stop':
        texto = ''.join(bloques[i] for i in sorted(bloques))
        print(f"texto: {texto}")
        print(f"stop_reason: {stop_reason}")
        print(f"input_tokens: {input_tokens}")
        print(f"output_tokens: {output_tokens}")
    # ping, content_block_start y content_block_stop no aportan nada
