class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_symmetrical(root):
    return is_symmetrical_core(root, root)


def is_symmetrical_core(root1,root2):
    if not root1 and not root2:
        return True

    if not root2 or not root2:
        return False

    if root1.value != root2.value:
        return False

    return is_symmetrical_core(root1.left,root2.right) and is_symmetrical_core(root1.right, root2.left)



if __name__ == "__main__":
    node7 = TreeNode(5)
    node6 = TreeNode(7)
    node5 = TreeNode(7)
    node4 = TreeNode(5)
    node3 = TreeNode(6, left=node6, right=node7)
    node2 = TreeNode(6, left=node4, right=node5)
    node1 = TreeNode(8, left=node2, right=node3)
    root = node1
    print(is_symmetrical(root))

    print()

    node7 = TreeNode(5)
    node6 = TreeNode(7)
    node5 = TreeNode(7)
    node4 = TreeNode(5)
    node3 = TreeNode(9, left=node6, right=node7)
    node2 = TreeNode(6, left=node4, right=node5)
    node1 = TreeNode(8, left=node2, right=node3)
    root = node1
    print(is_symmetrical(root))

    print()

    node6 = TreeNode(7)
    node5 = TreeNode(7)
    node4 = TreeNode(7)
    node3 = TreeNode(7, left=node6)
    node2 = TreeNode(7, left=node4, right=node5)
    node1 = TreeNode(7, left=node2, right=node3)
    root = node1
    print(is_symmetrical(root))