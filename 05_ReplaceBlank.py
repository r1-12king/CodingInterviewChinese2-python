def replace_space(string):
    if not string:
        return ""

    originalLength = len(string)
    blankLength = string.count(' ')
    string = list(string)
    string = string+[None]*blankLength*2

    newLength = originalLength+blankLength*2
    p1 = originalLength-1
    p2 = newLength-1

    while p1>=0 and p1!=p2:
        if string[p1] != ' ':
            string[p2] = string[p1]
            p2-=1
        else:
            string[p2-2:p2+1] = ['%','2','0']
            p2-=3
        p1-=1

    return "".join(string)

if __name__ == '__main__':
    print(replace_space("hello github!"))

