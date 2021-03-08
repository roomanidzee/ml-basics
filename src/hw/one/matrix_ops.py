
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

def stupid_transformation(X, a=1):

    Y = list(reversed(X))

    for index, elem in enumerate(X):
        if index % 2 != 0:
            Y[index] = elem

    for index, elem in enumerate(Y):
        if index % 2 != 0:
            Y[index] = a
        
        if index % 2 == 0:
            Y[index] = elem ** 3

    final_arr = X + Y
    return list(reversed(final_arr))

def transformation(X, a=1):

    new_arr = np.flip(X)

    new_arr[new_arr % 2 == 1] = a
    new_arr[new_arr % 2 == 0] ** 3

    return np.flip(np.concatenate((X, new_arr)))

