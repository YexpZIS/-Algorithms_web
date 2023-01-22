import sys
import pytest

sys.path.append(sys.path[0] + '/../../')
from algorithms.fuzzy_search import *

common_args = ('word1, word2, result', [
                ('', '', 0),
                ('word', 'word', 0),
                ('foo', 'baz', 3),
                ('foa', 'foo', 1),
])

@pytest.mark.parametrize(*common_args)
def test_fuzzy_search(word1, word2, result):
    assert fuzzy_search(word1, word2) == result