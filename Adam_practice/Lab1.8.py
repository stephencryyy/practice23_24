def find_neighbors(matrix, row, col):
    rows,cols = len(matrix), len(matrix[0])
    neighbors = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))

    return neighbors


# Пример использования
my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_index, col_index = 0, 0  # Индексы элемента 5
neighbors = find_neighbors(my_matrix, row_index, col_index)

print(f"Соседи элемента ({row_index}, {col_index}):")
for neighbor_row, neighbor_col in neighbors:
    print(f"({neighbor_row}, {neighbor_col})")
