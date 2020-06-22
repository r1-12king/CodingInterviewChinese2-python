def scan_unsigned_int(str, index):
    # start_index == index 用来标注是否有数位
    start_index = index
    while index<len(str) and str[index] in "0123456789":
        index+=1

    # 当str中存在若干0-9的数字时，返回true
    return index != start_index,index


def scan_int(str, index):
    if index<len(str) and str[index] in ['-','+']:
        index+=1

    return scan_unsigned_int(str, index)



def isNum(str):
    """
    数字的格式可以用A[.[B]][e|EC]或者.B[e|EC]表示，其中A和C都是
    整数（可以有正负号，也可以没有），而B是一个无符号整数
    """
    if not str:
        return False
    # 对A，A可以有或者没有
    index = 0
    result, index = scan_int(str,index)
    if index<len(str) and str[index] == '.':
        # 如果有B,B是无符号整数
        index+=1
        has_float,index =  scan_unsigned_int(str,index)
        result = result or has_float

    if index<len(str) and str[index] in ['e','E']:
        index+=1
        has_exp, index = scan_int(str,index)
        result = result and has_exp

    return result and index == len(str)


if __name__ == "__main__":
    print(isNum("+100"))
    print(isNum("5e2"))
    print(isNum("-123"))
    print(isNum("3.1415"))
    print(isNum("-1E-16"))
    print(isNum("12e"))
    print(isNum("1a3.14"))
    print(isNum("1.2.3"))
    print(isNum("+-5"))