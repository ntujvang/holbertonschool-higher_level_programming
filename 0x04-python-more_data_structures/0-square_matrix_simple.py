#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new.append([n * n for n in i])
    return new
