import sys
from flask import render_template, request, json

from views import info_format

sys.path.append(sys.path[0] + "/../../")
from algorithms.fuzzy_search import *
_info = info_format.InfoDTO('Levenshtein distance','/fuzzy_search','It is defined as the minimum number of single-character operations (namely insertions, deletions, substitutions) required to transform one sequence of characters into another.')

def get_info():
    return _info

def fuzzy_search():
    return render_template('algorithms/fuzzy_search.html', title = _info.name)

def fuzzy_search_api():
    if request.method == 'POST' and 'str_1' in request.json and 'str_2' in request.json:
        try:
            str_1, str_2 = request.json['str_1'], request.json['str_2']
            result = get_difference(str_1, str_2)
        except Exception:
            result = -1

        return {'result': result}