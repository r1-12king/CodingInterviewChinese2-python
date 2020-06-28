def get_max_value1(matrix):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = matrix[0][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    return dp[rows - 1][cols - 1]


def get_max_value2(matrix):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    m_value = [0] * cols

    for i in range(rows):
        for j in range(cols):
            up = 0
            left = 0
            if i > 0:
                up = m_value[j]
            if j > 0:
                left = m_value[j - 1]
            # print(m_value)
            m_value[j] = matrix[i][j] + max(up, left)

    return m_value[-1]


if __name__ == '__main__':
    res = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(get_max_value1(res))
    print(get_max_value2(res))
