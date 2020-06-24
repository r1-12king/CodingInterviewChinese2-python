class TreeNode:

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def has_sub_tree(root1, root2):
    result = False

    if root1 and root2:
        if root2.val == root1.val:
            result = does_tree1_has_tree2(root1, root2)
        if(not result):
            result = does_tree1_has_tree2(
                root1.left, root2) or does_tree1_has_tree2(roo1.right, root2)

    return result


def does_tree1_has_tree2(head1, head2):
    if head2 == None:
        return True
    if head1 == None:
        return False

    if head1.val != head2.val:
        return False

    return does_tree1_has_tree2(head1.left, head2.left) and does_tree1_has_tree2(head1.right, head2.right)


if __name__ == "__main__":
    tree1_7 = TreeNode(7)
    tree1_6 = TreeNode(4)
    tree1_5 = TreeNode(2, left=tree1_6, right=tree1_7)
    tree1_4 = TreeNode(9)
    tree1_3 = TreeNode(7)
    tree1_2 = TreeNode(8, left=tree1_4, right=tree1_5)
    tree1_1 = TreeNode(8, left=tree1_2, right=tree1_3)
    tree1 = tree1_1

    tree2_3 = TreeNode(2)
    tree2_2 = TreeNode(9)
    tree2_1 = TreeNode(8, left=tree2_2, right=tree2_3)
    tree2 = tree2_1

    print(has_sub_tree(tree1, tree2))
