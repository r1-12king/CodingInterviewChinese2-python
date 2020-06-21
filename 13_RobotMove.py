def movingCount(matrix, k):
    if not matrix or len(matrix[0]) == 0:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False] * cols for i in range(rows)]

    count = movingCountCore(matrix, k, (0, 0), visited)
    return count


def movingCountCore(matrix, k, matrix_indices, visited):
    count = 0
    i, j = matrix_indices
    if check(matrix, k, matrix_indices, visited):
        visited[i][j] = True
        count = 1 + movingCountCore(matrix, k, (i, j + 1), visited) + \
            movingCountCore(matrix, k, (i, j - 1), visited) + \
            movingCountCore(matrix, k, (i - 1, j), visited) + \
            movingCountCore(matrix, k, (i + 1, j), visited)

    return count


def check(matrix, k, matrix_indices, visited):
    i, j = matrix_indices
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (getDigitSum(i) + getDigitSum(j)) <= k and not visited[i][j]:
        return True
    return False


def getDigitSum(num):
    sum_ = 0
    while num > 0:
        sum_ += num % 10
        num = num // 10
    return sum_


if __name__ == '__main__':
    rows = 2
    cols = 2
    matrix = [[0 for _ in range(cols)]for _ in range(rows)]
    res = movingCount(matrix, 1)
    print(res)
