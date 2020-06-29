def reverse_sentence_1(string):
    """
    python 语法糖
    """
    if not string:
        return ""

    return " ".join((string.split(' '))[::-1])


def reverse_sentence_2(string):
    """
    先反转所有的字符，再对每个单词进行反转
    """
    if not string:
        return ""

    list_str = list(string)
    begin = 0
    end = len(list_str) - 1
    reverse(list_str, begin, end)

    begin = 0
    end = 0
    while begin < len(list_str) - 1:
        if list_str[begin] == " ":
            begin += 1
            end += 1
        elif list_str[end] == " " or end == len(list_str) - 1:
            end -= 1
            reverse(list_str, begin, end)
            end += 1
            begin = end
        else:
            end += 1
    return "".join(list_str)


def reverse(arr, begin, end):
    while begin<end:
        arr[begin],arr[end] = arr[end],arr[begin]
        begin+=1
        end-=1

    return arr

if __name__ == "__main__":
    print(reverse_sentence_1("I am a student."))
    print(reverse_sentence_2("I am a student."))
