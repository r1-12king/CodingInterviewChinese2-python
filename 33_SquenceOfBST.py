class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def verify_squence_of_BST(nums):
    if not nums:
        return False

    lens = len(nums)

    root = nums[lens-1]
    f = 0
    for i in range(0,lens-1):
        if nums[i]>root:
            f = i
            break
    for j in range(f,lens-1):
        if nums[j]<root:
            return False

    left = True 
    if f>0:
        left = verify_squence_of_BST(nums[:f])
    right = True
    if f<lens-1:
        right = verify_squence_of_BST(nums[f+1:])

    return left and right


if __name__ == "__main__":
    print(verify_squence_of_BST([5, 7, 6, 9, 11, 10, 8]))
    print(verify_squence_of_BST([7, 4, 6, 5]))