
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


def test_stupid_sec_av(input_arr, sec_output_arr):
    assert stupid_sec_av(input_arr) == sec_output_arr

def test_sec_av(input_arr, sec_output_arr):

    input_arr = np.array(input_arr)
    output_arr = np.array(sec_output_arr)

    assert sec_av(input_arr).all() == output_arr.all()

def test_stupid_transformation(transform_input_arr, transform_output_arr):
    assert stupid_transformation(transform_input_arr) == transform_output_arr

def test_transformation(transform_input_arr, transform_output_arr):

    input_arr = np.array(transform_input_arr)
    output_arr = np.array(transform_output_arr)

    assert transformation(input_arr).all() == output_arr.all()
