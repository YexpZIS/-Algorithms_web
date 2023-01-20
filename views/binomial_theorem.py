import sys
from flask import render_template, request, json

from views import info_format

sys.path.append(sys.path[0] + '/../../')
from algorithms.binomial_theorem import *

_info = info_format.InfoDTO('Binomial theorem', '/binomial_theorem', 'Used to decompose into separate terms a non-negative integer power of the sum of two variables')

def get_info():
    return _info

def binomial_theorem():
    return render_template('algorithms/binomial_theorem.html', title = _info.name)


def api_binomial_theorem():
    if request.method == 'POST' and 'expression' in request.json:
        expression = request.json['expression']
        
        try:
            result = open_brackets(expression)
        except Exception:
            result = 'Errore'
        return {'result' : result}
