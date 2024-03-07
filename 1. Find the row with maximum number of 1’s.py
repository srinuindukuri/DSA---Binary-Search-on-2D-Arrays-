# Problem Statement: You have been given a non-empty grid ‘mat’ with ‘n’ rows and ‘m’ columns consisting of only 0s and 1s.
# All the rows are sorted in ascending order.
# Your task is to find the index of the row with the maximum number of ones.
# Note: If two rows have the same number of ones, consider the one with a smaller index.
# If there’s no row with at least 1 zero, return -1.
# -------------------------------------------------------------------------------------------------------------------------

# Lower Bound Algorithm to find the 0 or 1s (In this case it's 1)

def LowerBound(arr, n, x):
    low = 0
    high = n-1
    ans = n
    while(low <= high):
        mid = (low+high) // 2
        if(arr[mid] >= x):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans


def RowWithMax1s(matrix, m, n):
    cnt_max = 0
    index = -1

    for i in range(n):
        cnt_ones = m - LowerBound(matrix[i], m, 1)
        if(cnt_ones > cnt_max):
            cnt_max = cnt_ones
            index = i
    return index


matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
n = 3
m = 3
print("The row with maximum no. of 1's is:", RowWithMax1s(matrix, n, m))
