def get_ugly_number(index):
    if index < 0:
        return 0

    uglyNums = [0] * index
    uglyNums[0] = 1
    nextUglyNumIndex = 1

    pMul2 = 0
    pMul3 = 0
    pMul5 = 0

    while nextUglyNumIndex < index:
        mins = min(uglyNums[pMul2] * 2, uglyNums[pMul3]
                   * 3, uglyNums[pMul5] * 5)
        uglyNums[nextUglyNumIndex] = mins

        while uglyNums[pMul2] * 2 <= uglyNums[nextUglyNumIndex]:
            pMul2 += 1
        while uglyNums[pMul3] * 3 <= uglyNums[nextUglyNumIndex]:
            pMul3 += 1
        while uglyNums[pMul5] * 5 <= uglyNums[nextUglyNumIndex]:
            pMul5 += 1

        nextUglyNumIndex += 1

    return uglyNums[-1]


if __name__ == '__main__':
    res = get_ugly_number(1500)
    print(res)
