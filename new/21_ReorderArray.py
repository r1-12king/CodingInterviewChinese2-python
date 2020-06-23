def record(arr, function):
    if not arr:
        return None

    left = 0
    right = len(arr)-1
    while left<right:
        while left<right and function(arr[left]):
            left+=1
        while left<right and not function(arr[right]):
            right-=1
        if left<right:
            arr[left],arr[right] = arr[right],arr[left]


def isEven(num):
    return num & 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    record(nums, isEven)
    print(nums)