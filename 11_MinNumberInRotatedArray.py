def find_in_order(arr, start, end):
    min_ = arr[start]
    for i in range(start+1,end+1):
        if min_ > arr[i]:
            min_ = arr[i]
    return min_


def find_min_in_rotate_arr(arr):
    p1 = 0
    p2 = len(arr)-1

    while arr[p1]>=arr[p2]:
        if p2-p1==1:
            return arr[p2]

        mid = (p1+p2)//2
        if arr[p1] == arr[p2] and arr[p1] == arr[mid]:
            return find_in_order(arr,p1,p2)

        if arr[p1]<=arr[mid]:
            p1 = mid
        elif arr[p2]>=arr[mid]:
            p2 = mid

    return arr[mid]


if __name__ == "__main__":
    print(find_min_in_rotate_arr([3, 4, 5, 1, 2]))
    print(find_min_in_rotate_arr([1, 1, 0, 1, 1]))