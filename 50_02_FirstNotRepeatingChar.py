def first_not_repeating_char2():
    maps = {}
    strs = ""
    while True:
        i = input()
        strs+=i

        if i not in maps:
            maps[i] = 1
        else:
            maps[i] = -1

        for i in strs:
            if maps[i] == 1:
                print(i)
                break



if __name__ == '__main__':
    first_not_repeating_char2()