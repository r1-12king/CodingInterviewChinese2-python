class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_path(root, sums):
    if not root:
        return []
    path = []
    curSum = 0
    find_path_core(root,sums,path,curSum)



def find_path_core(root,sums,path,curSum):
    curSum += root.value
    path.append(root.value)

    if not root.left and not root.right:
        if curSum == sums:
            print(path)
    else:
        if root.left:
            find_path_core(root.left,sums,path,curSum)
        if root.right:
            find_path_core(root.right,sums,path,curSum)

    path.pop()


if __name__ == "__main__":
    node5 = TreeNode(7)
    node4 = TreeNode(4)
    node3 = TreeNode(12)
    node2 = TreeNode(5, node4, node5)
    node1 = TreeNode(10, node2, node3)
    root = node1
    find_path(root, 22)