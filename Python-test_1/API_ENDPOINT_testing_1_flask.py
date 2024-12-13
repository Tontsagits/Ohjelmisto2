# API Endpoint testing 1 - Flask and parameters after ? mark in URL

from flask import Flask, request

app = Flask(__name__)


# määritetään endpoint eli päätepiste
@app.route('/summa')
# summa funktio, ajetaan kun kutsutaan endpointtia summa
def summa():
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1 + luku2
    return str(summa)


if __name__ == '__main__':
    # käynnistetään taustapalvelu
    # voisi olla myös 'localhost'
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
