def create_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        array_2d = [list(line.strip()) for line in file]
    return array_2d


def get_diagonals(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    diagonals = []

    # przekątne z lewej do prawej
    for d in range(rows + cols - 1):
        diagonal = []
        for r in range(max(0, d - cols + 1), min(rows, d + 1)):
            c = d - r
            diagonal.append(matrix[r][c])
        diagonals.append(''.join(diagonal))

    # przekątne z prawej do lewej
    for d in range(rows + cols - 1):
        diagonal = []
        for r in range(max(0, d - cols + 1), min(rows, d + 1)):
            c = cols - 1 - (d - r)
            diagonal.append(matrix[r][c])
        diagonals.append(''.join(diagonal))

    return diagonals


def extract_words_from_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # słowa z wierszy
    row_words = [''.join(row) for row in matrix]

    # słowa z kolumn
    col_words = [''.join(matrix[r][c] for r in range(rows)) for c in range(cols)]

    return row_words + col_words


def find_word_in_both_direction(text):
    quantity = count_word_occurrences(text, word_to_find)
    reversed_text = ''.join(reversed(text))
    quantity += count_word_occurrences(reversed_text, word_to_find)
    return quantity


def count_word_occurrences(text, word):
    return text.lower().count(word.lower())


summary = 0
word_to_find = "XMAS"

file_path = 'input.txt'
matrix = create_matrix_from_file(file_path)

columns_rows_words = extract_words_from_matrix(matrix)
diagonals = get_diagonals(matrix)
all_strings = columns_rows_words + diagonals

for word in all_strings:
    summary += find_word_in_both_direction(word)

print("Answer: ", summary)
