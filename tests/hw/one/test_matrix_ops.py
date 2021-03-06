
import numpy as np

from src.hw.one.matrix_ops import *

def test_simple_mult(matrix_one, matrix_two, matrix_result):

    actual_result = mult(matrix_one, matrix_two)

    assert actual_result == matrix_result

def test_np_mult(matrix_one, matrix_two, matrix_result):

    np_mat_one = np.matrix(matrix_one)
    np_mat_two = np.matrix(matrix_two)
    expected_result = np.matrix(matrix_result)

    assert np_mult(np_mat_one, np_mat_two).all() == expected_result.all()


def test_stupid_sec_av():

    input_arr = [1, 2, 3, 4 , 5, 6]
    output_arr = [1, 1.5, 2, 2.5, 3, 3.5]

    assert stupid_sec_av(input_arr) == output_arr

def test_sec_av():

    input_arr = np.array([1, 2, 3, 4 , 5, 6])
    output_arr = np.array([1, 1.5, 2, 2.5, 3, 3.5])

    assert sec_av(input_arr).all() == output_arr.all()
