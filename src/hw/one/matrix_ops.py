
import numpy as np

def mult(a, b):

    zip_b = list(zip(*b))

    return [
        [
            sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
            for col_b in zip_b
        ] for row_a in a
    ]

def np_mult(a, b):
    return a * b

def stupid_sec_av(A):

    return [
        sum(A[0:i + 1]) / (i + 1)
        for i in range(len(A))
    ]

def sec_av(A):

    new_arr = np.zeros(A.shape)

    limit = A.shape[0]

    for i in range(limit):
        new_arr[i] = np.sum(A[0:i + 1]) / (i + 1)

    return new_arr
