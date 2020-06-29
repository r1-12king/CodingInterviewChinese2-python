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


def is_balance_tree(root):
    """
    递归，每个节点重复遍历多次，复杂度高
    """
    if not root:
        return True

    lefts = tree_depth(root.left)
    rights = tree_depth(root.right)
    dis = abs(lefts-rights)
    if dis>1:
        return False

    return is_balance_tree(root.left) and is_balance_tree(root.right)



def is_balance_tree_2(root):
    return dfs(root) != -1


def dfs(root):
    if not root:
        return 0
    lefts = dfs(root.left)
    if lefts == -1:
        return -1
    rights = dfs(root.right)
    if rights == -1:
        return -1
    if abs(lefts-rights)>1:
        return -1
    return max(lefts,rights)+1



if __name__ == "__main__":
    node7 = TreeNode(7)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node7)
    node4 = TreeNode(4)
    node3 = TreeNode(3, None, node6)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)
    root = node1

    print(is_balance_tree(root))
    print(is_balance_tree_2(root))
