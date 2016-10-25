import numpy as np


def complex_hermitian_matrix_generation(dim):
    real_values = np.random.random_integers(-10, 10, size=(dim, dim))
    im_values = np.random.random_integers(-10, 10, size=(dim, dim))
    A = np.matrix(real_values + 1j*im_values)
    hermitian_matrix = (1/2)*(A + (A.H)) # le .H prend le conjugué puis la transposé
    return hermitian_matrix


def real_hermitian_matrix_generation(dim):
    A = np.matrix(np.random.random_integers(-10, 10, size=(dim, dim)))
    symetric_matrix = (1/2)*(A + (A.T))
    return symetric_matrix


def real_GUE(dim):
    A = np.random.randn(dim, dim)
    A_sym = np.triu(A) + np.triu(A, 1).T
    return A_sym


if __name__ == '__main__':
    print(np.zeros((2,3,4)))