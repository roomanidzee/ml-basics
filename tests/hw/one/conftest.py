
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

@pytest.fixture
def input_arr():
    return [1, 2, 3, 4 , 5, 6]

@pytest.fixture
def sec_output_arr():
    return [1, 1.5, 2, 2.5, 3, 3.5]

@pytest.fixture
def transform_input_arr():
    return [1, 2, 3, 4, 5, 6]

@pytest.fixture
def transform_output_arr():
    return [1, 8, 1, 64, 1, 216, 6, 5, 4, 3, 2, 1]
