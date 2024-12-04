def create_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        array_2d = [list(line.strip()) for line in file]
    return array_2d


def has_left_right_word(matrix, i, j):
    if (matrix[i - 1][j - 1] == 'M' and matrix[i + 1][j + 1] == 'S') or (
            matrix[i - 1][j - 1] == 'S' and matrix[i + 1][j + 1] == 'M'):
        return True
    else:
        return False


def has_right_left_word(matrix, i, j):
    if (matrix[i + 1][j - 1] == 'M' and matrix[i - 1][j + 1] == 'S') or (
            matrix[i + 1][j - 1] == 'S' and matrix[i - 1][j + 1] == 'M'):
        return True
    else:
        return False


def find_words_in_diagonal(matrix, i, j):
    if has_left_right_word(matrix, i, j) and has_right_left_word(matrix, i, j):
        return True
    else:
        return False


summary = 0

file_path = 'input.txt'
matrix = create_matrix_from_file(file_path)

rows = len(matrix)
cols = len(matrix[0])

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if matrix[i][j] == 'A' and find_words_in_diagonal(matrix, i, j):
            summary += 1

print("Answer: ", summary)
