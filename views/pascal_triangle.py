import sys
from flask import render_template, request, json

from views import info_format

sys.path.append(sys.path[0] + '/../../')
from algorithms.pascal_triangle import *

_info = info_format.InfoDTO('Pascal\'s triangle', '/pascal_triangle', 'It serves to raise a binomial to any power. Consists of binomial coefficients.')

def get_info():
    return _info

# TODO 
#
#
#


def pascal_triangle():
    return render_template('algorithms/binomial_theorem.html', title = _info.name)