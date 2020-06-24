def print_matrix(matrix):
    if not matrix:
        return

    res = []

    top, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

    while True:
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1
        if top >down:
            break

        for i in range(top, down+1):
            res.append(matrix[i][right])
        right -= 1
        if left >right:
            break

        for i in range(right, left - 1, -1):
            res.append(matrix[down][i])
        down -= 1
        if top > down:
            break

        for i in range(down, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
        if left >right:
            break

    return res

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    res = print_matrix(matrix)
    print(res)
