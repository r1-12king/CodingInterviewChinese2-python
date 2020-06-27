def duplicate2(nums):
    """
    题目二 不修改数组找出重复的数字
    时间O(n * log n), 空间O(1)
        不保证找到所有重复数字
    """
    if not nums:
        return -1

    for num in nums:
        if num < 1 or num > len(nums) - 1:
            return -1

    start = 1
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        count = count_range(nums, start, mid)
        if start == end:
            if count>1:
                return start
            else:
                break
        if count > mid-start+1:
            end = mid
        else:
            start = mid+1

    return -1

def count_range(nums, start, end):
    """
    O(n)
    """
    count = 0
    for num in nums:
        if start <= num <= end:
            count += 1
    return count


if __name__ == "__main__":
    print(duplicate2([2, 3, 1, 2, 5, 3]))
    print(duplicate2([2, 1, 1]))