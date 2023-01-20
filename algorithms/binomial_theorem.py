import re
from algorithms import pascal_triangle

from time import time

# reg = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')
# reg = re.compile(r'\((-?\d*)([a-zA-Z]+)\+?(-?\d+)\)\^(\d+)')
# reg = re.compile(r'\((-?\d*)([a-zA-Z]+)\+?(-?\d*)([a-zA-Z]?)\)\^(\d+)')
reg = re.compile(r'\((-?\d*\.?\d*)([a-zA-Z]+)\+?(-?\d*\.?\d*)([a-zA-Z]?)\)\^(\d+)')

def get_degree(n):
    return [[j, i] for i, j in enumerate(range(n, -1, -1))]

def parse(text):
    args = reg.findall(text)
    if args:
        args = list(*args)
        return {'first':{'char': args[1], 'number': parse_float(args[0])}, 
            'second': {'char': args[3], 'number': parse_float(args[2])}, 
            'degree': int(args[4])}
    else:
        raise ValueError('Invalid formula format')

def parse_float(number):
    if not number in ['', '-']:
        return float(number)
    else:
        return float(number + '1')

def open_brackets(expression):
    expression = parse(expression)
    coefficients = pascal_triangle.get_pascal_triangle(expression['degree'])
    degrees = get_degree(expression['degree'])

    result = ''
    
    for i, _ in enumerate(coefficients):
        coef = coefficients[i] * \
            expression['first']['number']**degrees[i][0] * \
            expression['second']['number']**degrees[i][1]
        
        coef = round(coef, 2)
        
        first_arg = format_char(expression['first']['char'], degrees[i][0], coef)
        second_arg = format_char(expression['second']['char'], degrees[i][1], coef)
        
        result +=format_number(coef, i, first_arg + second_arg) + first_arg + second_arg

    # print(expression)
    return result

def format_char(char, degree, number):
    if char == '' or degree == 0 or not number :
        return ''
    elif degree == 1:
        return char
    else:
        return f'{char}^{degree}'

def format_number(number, index, char):
    if not char and not number:
        return ''
    elif number == 1 and char != '' and index == 0:
        return ''
    elif number == 1 and char != '':
        return '+'
    elif number == -1 and char != '':
        return '-'
    elif number > 0 and index > 0:
        return f'+{number}'
    return str(number)

if __name__ == '__main__':
    
    start = time()
    print(open_brackets('(-30n+100)^1'))
    print(open_brackets('(-3n+1)^2'))
    print(open_brackets('(-3n+m)^3'))
    print(open_brackets('(-x-y)^2'))
    print(open_brackets('(-2.1x-6.2y)^2'))
    print(open_brackets('(-0n+0m)^4'))
    print(open_brackets('(-3n+0m)^4'))

    print(open_brackets('(x+y)^5'))
    
    
    print(open_brackets('(-5m+3)^4'))
    print(time() - start)

