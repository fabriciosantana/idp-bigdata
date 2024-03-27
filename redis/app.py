from flask import Flask
import redis

app = Flask(__name__)
db = redis.Redis(host='redis', port=6379)

# make redis
#redis_cache = redis.Redis(host='localhost', port=6379, db=0, password="redis_password")

@app.route('/')
def hello():
    count = db.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/sem-redis')
def hellow():
    #count = db.incr('hits')
    return 'Hello World! I have been seen times.'

@app.route('/set/<string:key>/<string:value>')
def set(key, value):
    if db.exists(key):
        pass
    else:
        db.set(key, value)
    return "OK"

@app.route('/get/<string:key>')
def get(key):
    if db.exists(key):
        return db.get(key)
    else:
        return f"{key} is not exists"

@app.route('/hello')
def hello_world():
    return 'Hello, World123!'

@app.route('/redis')
def redis():
    try:
        db.set("alguma_chave", "algum_valor")
        valor = db.get("alguma_chave")
        app.logger.info(f'Valor obtido do Redis: {valor}')
        return 'Olá, mundo!'
    except:
        return 'Erro'

@app.route('/set_valor/<chave>/<valor>')
def set_valor(chave, valor):
    db.set(chave, valor)
    return f'Valor {valor} foi armazenado com a chave {chave}'

@app.route('/get_valor/<chave>')
def get_valor(chave):
    valor = db.get(chave)
    if valor:
        return f'Valor recuperado: {valor.decode("utf-8")}'
    else:
        return 'Chave não encontrada'

@app.route('/push_lista/<lista>/<valor>')
def push_lista(lista, valor):
    db.lpush(lista, valor)
    return f'Valor {valor} adicionado à lista {lista}'

@app.route('/pop_lista/<lista>')
def pop_lista(lista):
    valor = db.lpop(lista)
    if valor:
        return f'Valor retirado da lista {lista}: {valor.decode("utf-8")}'
    else:
        return f'Lista {lista} está vazia ou não existe'

@app.route('/listar_valores/<lista>')
def listar_valores(lista):
    valores = db.lrange(lista, 0, -1)
    return f'Valores na lista {lista}: {[valor.decode("utf-8") for valor in valores]}'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)