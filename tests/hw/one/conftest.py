
import pytest

import numpy as np

@pytest.fixture
def matrix_one():
    return [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

@pytest.fixture
def matrix_two():
    return [[1,2],[1,2],[3,4]]

@pytest.fixture
def matrix_result():
    return [[12, 18], [27, 42], [42, 66], [57, 90]]
