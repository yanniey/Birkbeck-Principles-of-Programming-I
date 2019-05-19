import pytest
from Q2 import *

def test_common_elements():
    assert common_elements([3,1,2],[2,4,3])==[2,3]
    assert common_elements([3,3,2],[3,3,4,5]) == [3]


test_common_elements()