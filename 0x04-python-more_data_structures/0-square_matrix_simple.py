#!/usr/bin/python3
# 0-square_matrix_simple.py
# Jullius Okeyo <jaykopiyo@gmail.com>

def square_matrix_simple(matrix=[]):
    matrix_copy = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_copy[i][j] = matrix[i][j] * matrix[i][j]
