import sys

# Always run from unit_testing_best_practice/test
sys.path += ['C:/Users/thoma/Documents/DSTI/MLOps/DSTI_MLOps/testing/prime_testing/src'] 

from prime import is_prime

def test_answer():
    assert is_prime(2) == True