import sys
import pytest

sys.path.append(sys.path[0] + '/../../')
from algorithms.pascal_triangle import *

common_args = ('number, sequence', [ 
                            (0, [1]), 
                            (1, [1, 1]),
                            (2, [1, 2, 1]),
                            (3, [1, 3, 3, 1]), 
                            (4, [1, 4, 6, 4, 1]),
                            (5, [1, 5, 10, 10, 5, 1]),
                            (14, [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]),
                            ])

# @pytest.mark.skip()
@pytest.mark.parametrize(*common_args)
def test_correct_triangle(number, sequence):
    assert get_pascal_triangle(number) == sequence

@pytest.mark.parametrize(*common_args)
def test_correct_triangle_cached(number, sequence):
    assert get_pascal_triangle_cached(number) == sequence

wrong_common_args = ('number', [ 
                                (-1), 
                                (-100),
                                ])

@pytest.mark.parametrize(*wrong_common_args)
def test_wrong_triangle(number):
    with pytest.raises(Exception):
        get_pascal_triangle(number)

@pytest.mark.parametrize(*wrong_common_args)
def test_wrong_triangle_cached(number):
    with pytest.raises(Exception):
        get_pascal_triangle_cached(number)