def find_nums_with_sum(arr, sums):
    """
    hashset
    """
    if not arr or len(arr)<2:
        return []

    sets = set()

    for i in arr:
        if sums-i in sets :
            return[sums-i,i]
        sets.add(i)


def find_nums_with_sum_2(arr,sums):
    """
    双指针
    """
    if not arr or len(arr)<2:
        return []
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[left]+arr[right] == sums:
            return [ arr[left],arr[right]]
        elif arr[left]+arr[right] > sums:
            right-=1
        else:
            left+=1



if __name__ == "__main__":
    print(find_nums_with_sum([1, 2, 4, 7, 11, 15], 15))
    print(find_nums_with_sum_2([1, 2, 4, 7, 11, 15], 15))