def count_inverse_pair(arr):
    if not arr:
        return []

    copy_arr = [x for x in arr]
    result = count_inverse_pair_core(arr, copy_arr, 0, len(arr) - 1)
    print(copy_arr)
    return result


def count_inverse_pair_core(arr, copy_arr, start, end):
    if start == end:
        copy_arr[start] == arr[start]
        return 0

    mid = (end-start)//2
    left_count = count_inverse_pair_core(arr, copy_arr, start, start+mid)
    right_count = count_inverse_pair_core(arr, copy_arr, start+mid+1, end)

    count = 0
    i = start+mid
    j = end
    index = end

    while i>=start and j>=start+mid+1:
        if arr[i]>arr[j]:
            copy_arr[index] = arr[i]
            count += j-start-mid
            i-=1
        else:
            copy_arr[index] = arr[j]
            j-=1

        index-=1

    while i >= start:
        copy_arr[index] = arr[i]
        i-=1
        index-=1

    while j>= mid+start+1:
        copy_arr[index] = arr[j]
        j -= 1
        index -= 1

    for i in range(start, end + 1):
        arr[i] = copy_arr[i]

    return left_count + right_count + count


if __name__ == "__main__":
    print(count_inverse_pair([7, 5, 6, 4]))