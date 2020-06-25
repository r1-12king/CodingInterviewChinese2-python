class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree_in_zigzag(root):
    if not root:
        return
    stack = [[],[]]
    cur = 0
    ano = 1
    stack[cur]= [root]

    while stack[0] or stack[1]:
        node = stack[cur].pop()
        print(node.value,end=" ")
        if cur == 0:
            if node.left:
                stack[ano].append(node.left)
            if node.right:
                stack[ano].append(node.right)

        else:
            if node.right:
                stack[ano].append(node.right)
            if node.left:
                stack[ano].append(node.left)

        if not stack[cur]:
            print()
            cur,ano = ano,cur


if __name__ == "__main__":
    node7 = TreeNode(11)
    node6 = TreeNode(9)
    node5 = TreeNode(7)
    node4 = TreeNode(5)
    node3 = TreeNode(10, left=node6, right=node7)
    node2 = TreeNode(6, left=node4, right=node5)
    node1 = TreeNode(8, left=node2, right=node3)
    root = node1

    print_tree_in_zigzag(root)