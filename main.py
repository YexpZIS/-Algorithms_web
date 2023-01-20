from flask import Flask, redirect, url_for, request, render_template, json
from collections import OrderedDict

from views import binomial_theorem, pascal_triangle


app = Flask(__name__)

modules = [binomial_theorem, pascal_triangle]
ALGORITHMS = []
for i in modules:
    ALGORITHMS.append(i.get_info())


@app.route('/')
def index():
    return render_template('index.html', title = 'Algorithms', items=ALGORITHMS)


binom = binomial_theorem.get_info()
app.add_url_rule(binom.link, view_func = binomial_theorem.binomial_theorem)
app.add_url_rule('/api' + binom.link, view_func = binomial_theorem.api_binomial_theorem, methods = ['POST'])

pascal = pascal_triangle.get_info()
app.add_url_rule(pascal.link, view_func = pascal_triangle.pascal_triangle)
app.add_url_rule('/api' + pascal.link, view_func = pascal_triangle.pascal_triangle_api, methods = ['POST'])

if __name__ == '__main__':

    app.run(debug = True, host='192.168.0.129')

# python -m venv venv
# source venv/bin/activate
# export FLASK_APP='__init__.py'
# flask --app __init__.py --debug run # auto reload server
# flask --app __init__.py --debug run --host=192.168.0.129

# TODO: дописать тесты, написать нечеткий поиск(fuzzy_search), доделать сортировки
# + загрузить все на сервер + начать читать книгу