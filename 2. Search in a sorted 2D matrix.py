# Problem Statement: You have been given a 2-D array ‘mat’ of size ‘N x M’ where ‘N’ and ‘M’ denote the number of rows and
# columns, respectively. The elements of each row are sorted in non-decreasing order.
# Moreover, the first element of a row is greater than the last element of the previous row (if it exists).
# You are given an integer ‘target’, and your task is to find if it exists in the given ‘mat’ or not.

# -------------------------------------------------------------------------------------------------------------------------

def SearchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = n*m-1
    while(low <= high):
        mid = (low+high) // 2
        row = mid // m
        column = mid % m

        if(matrix[row][column] == target):
            return True
        elif matrix[row][column] < target:
            low = mid+1
        else:
            high = mid-1
    return False


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = SearchMatrix(matrix, 8)
print("true" if result else "false")
