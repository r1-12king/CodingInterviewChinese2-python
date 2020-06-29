"""
从头到尾一次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数组的异或结果。因为其他数字都出现了两次，在异或中全部抵消了。
由于两个数字肯定不一样，那么异或的结果肯定不为0，也就是说这个结果数组的二进制表示至少有一个位为1。
我们在结果数组中找到第一个为1的位的位置，记为第n位。
现在我们以第n位是不是1为标准把元数组中的数字分成两个子数组，第一个子数组中每个数字的第n位都是1，而第二个子数组中每个数字的第n位都是0。

"""

def find_nums_appear_once(arr):
    if not arr or len(arr)<2:
        return []

    res = 0

    for i in arr:
        res = res^i

    index = find_first_bit_is_1(res)

    num1 = 0
    num2 = 0

    for i in arr:
        if is_bit_1(i,index):
            num1 = num1^i
        else:
            num2 = num2^i

    return num1,num2


def find_first_bit_is_1(num):
    """
    找到num的二进制位中最右边是1的位置
    """
    index_of_bit = 0
    while num != 0 and num & 1 == 0:
        num = num >> 1
        index_of_bit += 1
    return index_of_bit

def is_bit_1(num,index):
    """
    判断第index位是不是1
    """
    num = num>>index
    return num&1


if __name__ == "__main__":
    print(find_nums_appear_once([-8, -4, 3, 6, 3, -8, 5, 5]))