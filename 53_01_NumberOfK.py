def get_first_k(arr, k, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if arr[mid] > k:
        return get_first_k(arr, k, start, mid - 1)

    if arr[mid] < k:
        return get_first_k(arr, k, mid + 1, end)

    if arr[mid] == k:
        if mid == 0 or arr[mid - 1] != k:
            return mid
        return get_first_k(arr, k, start, mid - 1)

    return None


def get_last_k(arr, k, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if arr[mid] > k:
        return get_last_k(arr, k, start, mid - 1)

    if arr[mid] < k:
        return get_last_k(arr, k, mid + 1, end)

    if arr[mid] == k:
        if mid == len(arr) - 1 or arr[mid + 1] != k:
            return mid
        return get_last_k(arr, k, mid + 1, end)

    return None


def count_number_of_k(arr, k):
    if not arr:
        return None

    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return None

    index_first_k = get_first_k(arr, k, 0, len(arr) - 1)
    index_last_k = get_last_k(arr, k, 0, len(arr) - 1)

    if index_first_k is None or index_last_k is None:
        return None

    return index_last_k - index_first_k + 1


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 3, 3, 4, 5]
    print(count_number_of_k(arr, 3))
