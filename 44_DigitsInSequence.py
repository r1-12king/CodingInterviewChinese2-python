def digit_at_index(index):
    if index < 0:
        return -1

    digit = 1
    while True:
        nums = count_of_int(digit)
        if index < nums * digit:
            return digit_at_index_core(index, digit)
        else:
            index -= nums * digit
            digit += 1

    return -1


def count_of_int(n):
    """
        有多少个n位数
    """
    if n == 1:
        return 10
    count = 10**(n - 1)
    return 9 * count


def digit_at_index_core(index, digit):
    num = beginNum(digit) + index / digit
    index_from_right = digit - index % digit
    for i in range(1, index_from_right):
        num /= 10

    return int(num % 10)


def beginNum(digit):
    """
        获得m位数字的第一个数字，0,10,100,1000...
    """
    if digit == 1:
        return 0
    return 10**(digit - 1)


if __name__ == '__main__':
    print(digit_at_index(1001))
