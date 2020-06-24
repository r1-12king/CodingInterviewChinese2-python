class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def mirror_recursively(root):
    if not root:
        return None
    if not root.left and not root.right:
        return root

    root.left, root.right = root.right, root.left

    if root.left:
        mirror_recursively(root.left)
    if root.right:
        mirror_recursively(root.right)

def print_tree(root):
    if root is None:
        return

    print(root.value)
    print_tree(root.left)
    print_tree(root.right)


if __name__ == "__main__":
    node7 = TreeNode(value=11)
    node6 = TreeNode(value=9)
    node5 = TreeNode(value=7)
    node4 = TreeNode(value=5)
    node3 = TreeNode(value=10, left=node6, right=node7)
    node2 = TreeNode(value=6, left=node4, right=node5)
    node1 = TreeNode(value=8, left=node2, right=node3)
    root = node1
    print_tree(root)
    print()
    mirror_recursively(root)
    print_tree(root)