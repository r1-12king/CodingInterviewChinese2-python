def numberOf1_1(num):
    count = 0
    while num:
        if num & 1:
            count += 1
        num = num >> 1

    return count


def numberOf1_3(num):
    """
    建议
    """
    count = 0
    while num:
        count += 1
        num = num & (num - 1)

    return count


if __name__ == '__main__':
    print(numberOf1_1(6))
    print(numberOf1_3(6))