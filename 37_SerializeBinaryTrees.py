from queue import Queue

class TreeNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def serialize(root):
    """
    Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
    """
    if not root:
        return "#_"

    res = str(root.value)+"_"
    res += serialize(root.left)
    res += serialize(root.right)
    return res


def deserialize(data):
    """
    Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
    """

    def preOrder(pre):
        val = pre.pop(0)
        if val == "#":
            return None
        root = TreeNode(int(val))
        root.left = preOrder(pre)
        root.right = preOrder(pre)
        return root

    if not data:
        return None
    pre = data.rstrip('_').split('_')
    return preOrder(pre)


def print_tree_from_top_to_bottom2(root):
    """
    题目二： 分行从上到下打印二叉树
    """
    if root is None:
        return
    assert isinstance(root, TreeNode)

    node_queue = Queue()
    node_queue.put(root)
    n_node = 1
    next_n_node = 0
    while not node_queue.empty():
        node = node_queue.get()
        print(node.value, end=' ')

        if node.left:
            next_n_node += 1
            node_queue.put(node.left)

        if node.right:
            next_n_node += 1
            node_queue.put(node.right)

        n_node -= 1
        if n_node == 0:
            print()
            n_node = next_n_node
            next_n_node = 0


if __name__ == "__main__":
    node6 = TreeNode(6)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node5, node6)
    node2 = TreeNode(2, node4)
    node1 = TreeNode(1, node2, node3)
    root = node1
    res = serialize(root)
    print(res)
    new_root = deserialize(res)
    print_tree_from_top_to_bottom2(new_root)