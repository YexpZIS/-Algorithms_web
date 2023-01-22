from flask import Flask, redirect, url_for, request, render_template, json
from collections import OrderedDict

from views import binomial_theorem, pascal_triangle, fuzzy_search


app = Flask(__name__)

modules = [binomial_theorem, pascal_triangle, fuzzy_search]
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

search = fuzzy_search.get_info() 
app.add_url_rule(search.link, view_func = fuzzy_search.fuzzy_search)
app.add_url_rule('/api' + search.link, view_func = fuzzy_search.fuzzy_search_api, methods = ['POST'])

if __name__ == '__main__':

    app.run(debug = True, host='192.168.0.129')