def find_missing_number_1(arr):
    """
    异或，转变成只出现一次的数字
    方法一般般，只是想到这个题
    """
    if not arr or len(arr) == max(arr)+1:
        return None

    new = [i for i in range(len(arr)+1)]

    res = 0
    for i in new:
        res = res^i

    for j in arr:
        res = res^j

    return res


def find_missing_number_2(arr):
    """
    找出数组中第一个下标和数值不同的数
    """
    if not arr or len(arr) == max(arr)+1:
        return None

    left = 0
    right = len(arr)-1

    while left<=right:
        mid = left+((right-left)>>1)
        if arr[mid] != mid:
            if mid==0 or arr[mid-1]==mid-1:
                return mid
            right = mid-1
        else:
            left = mid+1

    return None


if __name__ == '__main__':
    print(find_missing_number_1([0, 1, 2, 3, 4, 6]))
    print(find_missing_number_2([0, 1, 2, 3, 4, 6]))