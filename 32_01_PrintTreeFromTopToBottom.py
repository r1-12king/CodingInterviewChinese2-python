class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree_from_top_to_bottom(root):
    res = []
    if not root:
        return res
    queue = [root]

    while queue:
        cur = queue.pop(0)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
        res.append(cur.value)

    return res



if __name__ == "__main__":
    node7 = TreeNode(11)
    node6 = TreeNode(9)
    node5 = TreeNode(7)
    node4 = TreeNode(5)
    node3 = TreeNode(10, left=node6, right=node7)
    node2 = TreeNode(6, left=node4, right=node5)
    node1 = TreeNode(8, left=node2, right=node3)
    root = node1

    res = print_tree_from_top_to_bottom(root)
    print(res)