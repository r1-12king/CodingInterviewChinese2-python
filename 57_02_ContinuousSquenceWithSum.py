def find_continuous_sequence(target):
    if target <= 0:
        return None

    res = []
    small = 1
    big = 2
    data = [1,2]
    while small <= (target) // 2:
        data = [i for i in range(small,big+1)]
        if sum(data) == target:
            res.append(data[:])
            big+=1
            data.append(big)
        elif sum(data) < target:
            big+=1
            data.append(big)
        else:
            small+=1
            data.pop(0)

    return res


if __name__ == '__main__':
    res = find_continuous_sequence(15)
    print(res)