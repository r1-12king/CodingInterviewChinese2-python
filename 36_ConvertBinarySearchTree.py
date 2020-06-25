class TreeNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def convert(root):
    if not root:
        return []

    last_node = None
    last_node = convert_core(root, last_node)

    while last_node and last_node.left:
        last_node = last_node.left

    return last_node


def convert_core(root, last_node):
    if not root:
        return
    cur = root
    if cur.left:
        last_node = convert_core(cur.left, last_node)

    if last_node:
        cur.left = last_node
        last_node.right = cur

    last_node = cur

    if cur.right:
        last_node = convert_core(cur.right, last_node)

    return last_node


def display(head):
    p = head
    while p:
        print(p.value, end=" ")
        if p.left:
            print(p.left.value, end=" ")
        if p.right:
            print(p.right.value, end=" ")
        print()
        p = p.right


if __name__ == "__main__":
    node7 = TreeNode(16)
    node6 = TreeNode(12)
    node5 = TreeNode(8)
    node4 = TreeNode(4)
    node3 = TreeNode(14, node6, node7)
    node2 = TreeNode(6, node4, node5)
    node1 = TreeNode(10, node2, node3)
    root = node1
    head = convert(root)
    display(head)
