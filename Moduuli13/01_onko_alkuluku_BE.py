# Ohjelmisto 2 - Moduuli 13 - Tehtävä 1 - Onko alkuluku, backend versio

from flask import Flask

app = Flask(__name__)


# toimiva URL esim http://127.0.0.1:3000/alkuluku/93
@app.route('/alkuluku/<numero>')
def alkuluku(numero):
    luku = int(numero)
    # oletetaan että on alkuluku
    isPrime = True
    # jos 1 niin ei ole
    if luku == 1:
        isPrime = False
    # jos jakolasku itseään pienemmällä menee tasan niin ei ole
    else:
        for i in range(2, luku):
            # return f"{luku} / {i} = {luku / i}"
            if luku % i == 0:
                isPrime = False
    vastaus = {
        "Number": luku,
        "isPrime": isPrime,
    }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
