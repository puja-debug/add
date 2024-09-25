def add_matrices(matrix_a, matrix_b):
    # Check if matrices are of the same size
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]

    # Perform the addition
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result

# Example usage
if __name__ == "__main__":
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix_b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    result = add_matrices(matrix_a, matrix_b)
    print("Resultant Matrix:")
    for row in result:
        print(row)
