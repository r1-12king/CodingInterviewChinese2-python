def reverse(arr, begin, end):
    while begin<end:
        arr[begin],arr[end] = arr[end],arr[begin]
        begin+=1
        end-=1

    return arr

def rotate_string(string, n):
    if not string or n<0:
        return string

    list_of_char = list(string)
    n = n%len(string)

    reverse(list_of_char, 0, n - 1)
    reverse(list_of_char, n, len(string) - 1)
    reverse(list_of_char, 0, len(string) - 1)
    return "".join(list_of_char)

if __name__ == "__main__":
    print(rotate_string("I am a student.",3))
