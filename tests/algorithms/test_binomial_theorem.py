import pytest
import sys


sys.path.append(sys.path[0] + '/../../')
from algorithms.binomial_theorem import *



@pytest.mark.parametrize('expression',[
                            ('(m+3)^2'),
                            ('(m+3n)^2'),
                            ('(5m+2n)^7'),
                            ('(100m+1)^229'),
                            ('  (10m+5)^3  '),
                            ('(1.234m+9.009n)^7'),
                            ])
def test_correct_regular_expression(expression):
    try:
        parse(expression)
        assert True
    except:
        assert False
           

@pytest.mark.parametrize('expression', [
                            (''),
                            ('a'),
                            ('()'),
                            ('a+b'),
                            ('d+5'),
                            ('5+5'),
                            ('(5+5)'),
                            ('(3+1)^n'),
                            ('(3+1)^1'),
                            ('(100m+1)^-229'),
                        ])
def test_wrong_regular_expression(expression):
    with pytest.raises(Exception):
        parse(expression)
