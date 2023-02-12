# Напишите функцию для транспонирования матрицы

array_matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]


def transposition_matrix(matrix):
    new_matrix = list(zip(*matrix))
    return new_matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
        

res = transposition_matrix(array_matrix)
print_matrix(res)

