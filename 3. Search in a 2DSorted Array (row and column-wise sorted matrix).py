# Problem Statement: You have been given a 2-D array ‘mat’ of size ‘N x M’ where ‘N’ and ‘M’ denote the number of rows
# and columns, respectively. The elements of each row and each column are sorted in non-decreasing order.
# But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists).
# You are given an integer ‘target’, and your task is to find if it exists in the given ‘mat’ or not.

# -----------------------------------------------------------------------------------------------------------------------

def SearchElement(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1

    # Traverse the matrix from (0, m-1):
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = SearchElement(matrix, 8)
print("true" if result else "false")
