def max_in_window(nums, size):
    res = []
    queue = []

    for i in range(size):
        if len(queue)!=0 and nums[i]>nums[queue[-1]]:
            queue.pop()
        queue.append(i)

    for i in range(size, len(nums)):
        res.append(nums[queue[0]])
        while len(queue)!=0 and nums[i]>nums[queue[-1]]:
            # 当窗口要将新的元素包含进来的时候，把窗口中比新元素值小的元素的下标都弹出
            queue.pop()
        while len(queue) != 0 and queue[0] <= i - size:
            # 如果队列包含的元素个数大于size 说明当前窗口左端已经把包括队头 弹出
            queue.pop(0)
        queue.append(i)

    res.append(nums[queue[0]])
    return res

if __name__ == '__main__':
    res = max_in_window([2,3,4,2,6,2,5,1],3)
    print(res)