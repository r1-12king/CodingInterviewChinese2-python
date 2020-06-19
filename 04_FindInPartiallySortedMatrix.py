def find(matrix, num):
    if len(matrix) == 0 or len(matrix[0])==0:
        return False

    row, col = len(matrix),len(matrix[0])
    i = 0
    j = col-1
    while i<row and j>=0:
        if matrix[i][j] == num:
            return True
        elif matrix[i][j] > num:
            j-=1
        else:
            i+=1
    return False

if __name__ == '__main__':
    matrix = [
    [1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]
    ]
    num = 4
    print(find(matrix,num))