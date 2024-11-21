import sys
# Always run from unit_testing_best_practice/test
sys.path += ['C:/Users/thoma/Documents/DSTI/MLOps/DSTI_MLOps/testing/unit_testing_best_practice/src'] 

from best_practice_samplesample import *

def test_answer():
    assert func(4) == 5

def test_answer_2():
    assert func_2(3) == 5