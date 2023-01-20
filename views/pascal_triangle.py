import sys
from flask import render_template, request, json

from views import info_format

sys.path.append(sys.path[0] + '/../../')
from algorithms.pascal_triangle import *

_info = info_format.InfoDTO('Pascal\'s triangle', '/pascal_triangle', 'It serves to raise a binomial to any power. Consists of binomial coefficients.')

def get_info():
    return _info

def pascal_triangle():
    return render_template('algorithms/pascal_triangle.html', title = _info.name)

def pascal_triangle_api():
    if request.method == 'POST' and 'number' in request.json:
        number = request.json['number']
        try:
            number = int(number)
            get_pascal_triangle_cached(int(number))
            result = get_cache()[:number]
        except Exception:
            result = []
        return {'result': result}