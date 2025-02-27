def createMatrix():
    """
    Function Description:
        Prompts the user to input values for a matrix
    Parameters:
        None
    Return:
        A multi-dimensional list representing the matrix
    """
    try:
        rows = int(input("Please enter the number of rows of the matrix: "))
        columns = int(input("Please enter the number of columns of the matrix: "))
    except ValueError:
        print("Invalid input. Please enter integers for rows and columns.")
        return createMatrix()

    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f'Enter row {i+1} as comma-separated values: ').split(',')))
                if len(row) != columns:
                    raise ValueError(f'Row must contain exactly {columns} values.')
                matrix.append(row)
                break
            except ValueError as e:
                print(e)

    return matrix


def multipleMatrix(matrixA, matrixB):
    """
    Function Description:
        Multiplies two matrices if compatible
    Parameters:
        matrixA: First matrix
        matrixB: Second matrix
    Returns:
        The matrix that is a result of the multiplication or None if multiplication is not possible
    """
    rowsA, colsA = len(matrixA), len(matrixA[0])
    rowsB, colsB = len(matrixB), len(matrixB[0])

    if colsA != rowsB:
        return None

    result = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result


def main():
    """
    Function Description:
        Main function to run the matrix multiplication program
    Return:
        The result of the matrix multiplication
    """
    while True:
        print("Enter the first matrix:")
        matrixA = createMatrix()

        print("\nEnter the second matrix:")
        matrixB = createMatrix()

        result = multipleMatrix(matrixA, matrixB)

        if result is None:
            print("\nMatrix multiplication is not valid. Please re-enter both matrices.\n")
        else:
            print("\nThe result of the matrix multiplication is:")
            for row in result:
                print(row)
            break

main()
