import random


"""
解法一：基于Partition函数的时间复杂度为O(n)的算法
（即top n/2思想）
（修改原数组）
"""
def partition(arr, start, end):
    if start<0 or end>len(arr):
        return None

    pvit = random.randint(start,end)
    arr[pvit],arr[start] = arr[start],arr[pvit]
    left = start+1
    right = end

    while True:
        while left<=right and arr[left]<=arr[start]:
            left+=1
        while left<=right and arr[right]>=arr[start]:
            right-=1
        if left>right:
            break
        arr[left],arr[right] = arr[right],arr[left]

    arr[start], arr[right] = arr[right], arr[start]

    return right

def check_more_than_half(arr,target):
    return arr.count(target)>len(arr)//2


def more_than_half_num_1(arr):
    if not arr:
        return

    mid = len(arr)>>1

    start = 0
    end = len(arr)-1
    index = partition(arr, start,end)

    while (index != mid):
        if index>mid:
            end = index-1
            index = partition(arr, start,end)
        else:
            start = index+1
            index = partition(arr, start,end)

    result = arr[mid]
    if check_more_than_half(arr,result):
        return result
    return 0


"""
解法二：根据数组特点找出时间复杂度为O(n)的算法
（不修改原数组）
"""
def more_than_half_num_2(arr):
    if not arr:
        return

    result = arr[0]
    times = 1

    for i in range(1,len(arr)):
        if times ==0:
            result = arr[i]
            times= 1
        else:
            if arr[i] == arr[i-1]:
                times+=1
            else:
                times-=1

    if check_more_than_half(arr,result):
        return result
    return 0

if __name__ == '__main__':
    print(more_than_half_num_1([1,2,3,2,2,2,5,4,2]))
    print(more_than_half_num_2([1,2,3,2,2,2,5,4,2]))