import copy

from pprint import pprint
from time import time

def get_pascal_triangle(number):
    if number < 0:
        raise ValueError('Value must be >= 0')

    number += 1

    triangle = [1] * (number)
    next_triangle = triangle[:]

    for i in range(number):
        for j in range(1, i):
            a = triangle[j - 1]
            b = triangle[j]
            
            next_triangle[j] = a + b

        triangle, next_triangle = next_triangle, triangle

    return triangle

cache = [[1], 
        [1, 1], 
        [1, 2, 1], 
        [1, 3, 3, 1],
        ]
def get_cache():
    return cache

def get_pascal_triangle_cached(number):
    if number < 0:
        raise ValueError('Value must be >= 0')
        
    global cache
    len_ = len(cache) - 1

    if len_  >= number:
        return cache[number]
    else:
        new_lines = list(calculate_pascal_triangle(len_ ,number, copy.copy(cache[-1])))
        cache += new_lines
        return cache[-1]
        

def calculate_pascal_triangle(start, stop, triangle):
    triangle += [1] * (stop - start)
    next_triangle = triangle[:]

    for i in range(start+1, stop+1):
        for j in range(1, i):
            a = triangle[j - 1]
            b = triangle[j]
            
            next_triangle[j] = a + b

        triangle, next_triangle = next_triangle, triangle
        yield triangle[: i + 1]

if __name__ == '__main__':
    # Speed test
    start = time()
    get_pascal_triangle(100)
    get_pascal_triangle(99)
    get_pascal_triangle(5)
    get_pascal_triangle(1)

    print('No cache:\t'+ str(time() - start))

    start = time()

    get_pascal_triangle_cached(100)
    get_pascal_triangle_cached(99)
    get_pascal_triangle_cached(5)
    get_pascal_triangle_cached(1)

    print('Cahced: \t'+ str(time() - start))

    # pprint(cache)
