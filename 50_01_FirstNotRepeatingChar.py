def first_not_repeating_char(s):
    maps = {}
    for i in s:
        if i not in maps:
            maps[i] = 1
        else:
            maps[i] += 1

    for i in s:
        if maps[i] == 1:
            return i

    return None


if __name__ == '__main__':
    res = first_not_repeating_char("qwertytrewqf")
    print(res)