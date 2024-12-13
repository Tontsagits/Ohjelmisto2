# API Endpoint testing 5 - request shows

from flask import Flask, request
import requests

app = Flask(__name__)


# http://127.0.0.1:3000/show?showname=Batman

@app.route('/show')
def show():
    args = request.args
    showname = str(args.get("showname"))
    pyynto = "https://api.tvmaze.com/search/shows?q=" + showname

    vastaus = {
        "luku1": luku1,
        "luku2": luku2,
        "summa": summa
    }

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
