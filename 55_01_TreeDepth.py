class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_depth(root):
    if not root:
        return 0

    lefts = tree_depth(root.left)
    rights = tree_depth(root.right)
    return max(lefts + 1, rights + 1)


if __name__ == "__main__":
    node7 = TreeNode(7)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node7)
    node4 = TreeNode(4)
    node3 = TreeNode(3, None, node6)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)
    root = node1

    print(tree_depth(root))
