def duplicate1(nums):
    """
    题目一 找出数组中重复的数字
    原地修改数组
    时间O(n), 空间O(1)
    """
    if not nums:
        return -1

    for num in nums:
        if num >= len(nums) or num < 0:
            return -1

    for index in range(len(nums)):
        while nums[index] != index:
            if nums[nums[index]] == nums[index]:
                # 找到重复数字
                return nums[index]
            nums[nums[index]], nums[index] = nums[index], nums[nums[index]]
            # 注意，下面这种是错的，，先修改了nums[index],再修改nums[nums[index]]会出错
            # nums[index], nums[nums[index]] = nums[nums[index]], nums[index]

    return None

if __name__ == "__main__":
    print(duplicate1([2, 3, 1, 2, 5, 3, 0]))
    print(duplicate1([2, 1, 0]))