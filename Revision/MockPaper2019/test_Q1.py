import pytest
from Q1 import *

def test_number_of_above_average():
    assert number_of_above_average(2,2,[[1,1],[2,4]]) == 1
    assert number_of_above_average(2,3,[[1,2,3],[4,5,6]]) ==3

test_number_of_above_average()