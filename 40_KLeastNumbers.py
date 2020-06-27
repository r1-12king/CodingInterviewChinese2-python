import random


"""
解法一：基于Partition函数的时间复杂度为O(n)的算法
只有当我们可以修改输入的数组时可用
"""
def partition(arr,start,end):
    i = ( start-1 )         # 最小元素索引
    pivot = arr[end]
    for j in range(start , end):
        # 当前元素小于或等于 pivot
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1

def get_least_numbers_1(arr,k):
    if not arr:
        return []

    start = 0
    end = len(arr)-1
    index = partition(arr,start,end)
    while index != k-1:
        if index < k-1:
            start = index+1
            index = partition(arr,start,end)
        else:
            end = index-1
            index = partition(arr,start,end)

    return arr[:k]



"""
解法二：时间复杂度为O(nlogk)的算法， 特别适合处理海量数据
（不改变原数组）
"""
def get_least_numbers_2(array, k):
    import heapq

    max_heap = []
    for x in array:
        heapq.heappush(max_heap, -x)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    for x in max_heap:
        print(-x, end=" ")


if __name__ == '__main__':
    print(get_least_numbers_1([1,2,3,4,5,6,7,8],3))
    print(get_least_numbers_2([1,2,3,4,5,6,7,8],3))