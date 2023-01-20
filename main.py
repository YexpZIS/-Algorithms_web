from flask import Flask, redirect, url_for, request, render_template, json
from collections import OrderedDict

from algorithms.binomial_theorem import open_brackets

from views import views


app = Flask(__name__)

ALGORITHMS = OrderedDict({'binomial_theorem': {'name': 'Binomial theorem', 'link': '/binomial_theorem', 'description': 'Used to decompose into separate terms a non-negative integer power of the sum of two variables'},
            'pascal_triangle': {'name': 'Pascal\'s triangle', 'link': '/pascal_triangle', 'description': 'It serves to raise a binomial to any power. Consists of binomial coefficients.'},
})

@app.route('/')
def index():
    return render_template('index.html', title = 'Algorithms', items=ALGORITHMS)

@app.route('/binomial_theorem')
def binomial_theorem():
    return render_template('algorithms/binomial_theorem.html', title = ALGORITHMS['binomial_theorem']['name'])


@app.route('/api/binomial_theorem', methods = ['POST'])
def api_binomial_theorem():
    if request.method == 'POST' and 'expression' in request.json:
        expression = request.json['expression']
        
        
        try:
            result = open_brackets(expression)
        except Exception:
            result = 'Errore'
        return {'result' : result}

app.add_url_rule('/test', view_func=views.test)


if __name__ == '__main__':
    
    app.run(debug = True, host='192.168.0.129')

# python -m venv venv
# source venv/bin/activate
# export FLASK_APP='__init__.py'
# flask --app __init__.py --debug run # auto reload server
# flask --app __init__.py --debug run --host=192.168.0.129

# TODO: дописать тесты, написать нечеткий поиск(fuzzy_search), доделать сортировки 
# + загрузить все на сервер + начать читать книгу