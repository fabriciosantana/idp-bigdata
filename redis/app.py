from flask import Flask
import redis
app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello_world():
    return 'Hello, World123!'

@app.route('/redis')
def redis():
    try:
        r.set("alguma_chave", "algum_valor")
        valor = r.get("alguma_chave")
        app.logger.info(f'Valor obtido do Redis: {valor}')
        return 'Olá, mundo!'
    except:
        return 'Erro'

@app.route('/set/<chave>/<valor>')
def set_valor(chave, valor):
    r.set(chave, valor)
    return f'Valor {valor} foi armazenado com a chave {chave}'

@app.route('/get/<chave>')
def get_valor(chave):
    valor = r.get(chave)
    if valor:
        return f'Valor recuperado: {valor.decode("utf-8")}'
    else:
        return 'Chave não encontrada'

@app.route('/push/<lista>/<valor>')
def push_lista(lista, valor):
    r.lpush(lista, valor)
    return f'Valor {valor} adicionado à lista {lista}'

@app.route('/pop/<lista>')
def pop_lista(lista):
    valor = r.lpop(lista)
    if valor:
        return f'Valor retirado da lista {lista}: {valor.decode("utf-8")}'
    else:
        return f'Lista {lista} está vazia ou não existe'

@app.route('/listar/<lista>')
def listar_valores(lista):
    valores = r.lrange(lista, 0, -1)
    return f'Valores na lista {lista}: {[valor.decode("utf-8") for valor in valores]}'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)