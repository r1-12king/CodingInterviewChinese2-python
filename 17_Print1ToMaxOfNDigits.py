def print_digits(digits):
    # res = "".join(digits).lstrip('0')
    # if res:
    #     print(res)
    isBeginning0 = True
    result = ""
    for n in digits:
        if isBeginning0 and n != '0':
            isBeginning0 = False
        if not isBeginning0:
            result+=n

    if result!="":
        print(result)


def print_1_to_max_of_n_digits(n):
    if n<=0:
        return

    digits = [0]*n
    print_digits_recursivly(digits,len(digits),0)


def print_digits_recursivly(digits,lens,index):
    if index == lens:
        print_digits(digits)
        return

    for i in range(10):
        digits[index] = str(i)
        print_digits_recursivly(digits,lens,index+1)


if __name__ == "__main__":
    print_1_to_max_of_n_digits(1)