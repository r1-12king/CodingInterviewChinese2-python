"""
    由于python3中sorted函数除去compare函数，无法自定义排序规则，所以使用内置的函数，将cmp函数转化为key的值

    Note：
        functools.cmp_to_key() 将 cmp函数 转化为 key。
        cmp函数的返回值 必须为 [1,-1,0]
"""

from functools import cmp_to_key


def compare(strNum1, strNum2):
    newStrNum1 = strNum1 + strNum2
    newStrNum2 = strNum2 + strNum1
    if newStrNum2 > newStrNum1:
        return -1
    elif newStrNum2 == newStrNum1:
        return 0
    else:
        return 1


def print_min_nums(nums):
    if not nums:
        return 0

    arr = [str(i) for i in nums]
    newarr = sorted(arr,key=cmp_to_key(compare))
    return "".join(newarr)


if __name__ == '__main__':
    print(print_min_nums([3,32,321]))