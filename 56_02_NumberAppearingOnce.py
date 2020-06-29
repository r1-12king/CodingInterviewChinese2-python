# 方法一
def find_num_appear_once(arr):
    """
    出现3次就不能再用异或的方法了，因为三个相同的数异或还是得到本身。但是还是可以采用位运算的思想，因为出现三次的数字每个位（0或者1）也是出现三次，因此可以每一位的和能够被3整除（对3取余为0）。所以如果把每个数的二进制表示的每一位加起来，对于每一位的和，如果能被3整除，那对应那个只出现一次的数字的那一位就是0，否则对应的那一位是1。

    我们需要用一个数组bitSum保存每一位的和，具体来讲实现过程是，先初始化为0，然后对于每个数字，遍历它二进制表示的每一位，如果这一位是1，bitSum对应的那一位就加1。
    """
    if not arr:
        return

    max_length = max([len(bin(x)) for x in arr])
    bits_count = [0] * max_length
    for x in arr:
        bit_mask = 1  # 对于每个数都从最低位开始判断
        for bit_index in range(max_length - 1, -1, -1):
            if x & bit_mask != 0:
                bits_count[bit_index] += 1
            bit_mask = bit_mask << 1

    result = 0
    for count in bits_count:
        result = result << 1  # 先把当前结果左移到高位
        result += count % 3  # 然后把当前位应该为0还是1填上去

    return result


# 方法二
def find_num_appear_once_2(nums):
    seen_once = seen_twice = 0
    for num in nums:
        # first appearance:
        # add num to seen_once
        # don't add to seen_twice because of presence in seen_once

        # second appearance:
        # remove num from seen_once
        # add num to seen_twice

        # third appearance:
        # don't add to seen_once because of presence in seen_twice
        # remove num from seen_twice
        seen_once = ~seen_twice & (seen_once ^ num)
        seen_twice = ~seen_once & (seen_twice ^ num)

    return seen_once


# 方法三，对方法二的解释
def find_num_appear_once_2_explain(nums):
    one = 0
    two = 0
    for num in nums:
        # two的相应的位等于1，表示该位出现2次
        two |= (one & num)
        # one的相应的位等于1，表示该位出现1次
        one ^= num
        # three的相应的位等于1，表示该位出现3次
        three = (one & two)
        # 如果相应的位出现3次，则该位重置为0
        two &= ~three
        one &= ~three
    return one


# 方法四
def find_num_appear_once_3(nums):
    """
    Hashset
    """
    return (3 * sum(set(nums)) - sum(nums)) // 2


# 方法五
from collections import Counter
def find_num_appear_once_4(nums):
    """
    Hashmap
    """
    hashmap = Counter(nums)
    for k in hashmap.keys():
        if hashmap[k] == 1:
            return k



if __name__ == '__main__':
    arr = [1,2,3,1,2,3,1,2,3,4]
    print(find_num_appear_once(arr))
    print(find_num_appear_once_2(arr))
    print(find_num_appear_once_2_explain(arr))
    print(find_num_appear_once_3(arr))
    print(find_num_appear_once_3(arr))


