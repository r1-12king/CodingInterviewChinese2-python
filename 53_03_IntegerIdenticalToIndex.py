def find_number_same_as_index(arr):
    if not arr:
        return None

    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return None

    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid

        if arr[mid] > mid:
            end = mid - 1

        if arr[mid] < mid:
            start = mid + 1
    return None

if __name__ == '__main__':
    print(find_number_same_as_index([-3, -1, 1, 3, 5]))