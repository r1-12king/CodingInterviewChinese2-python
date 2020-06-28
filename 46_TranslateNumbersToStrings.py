def get_translation_count(num):
    if num < 0:
        return 0

    strNum = str(num)
    lens = len(strNum)
    counts = [0] * lens

    for i in range(lens - 1, -1, -1):
        if i == lens - 1:
            counts[i] = 1
            continue

        count = counts[i + 1]
        value = (ord(strNum[i]) - ord('0')) * \
            10 + ord(strNum[i + 1]) - ord('0')
        if 10 <= value <= 25:
            if i == lens - 2:
                count += 1
            else:
                count += counts[i + 2]
        counts[i] = count

    return counts[0]

if __name__ == '__main__':
    print(get_translation_count(11258))
