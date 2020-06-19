class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

def set_relation(parent,left,right):
    parent.left = left
    parent.right = right
    left.parent = parent
    right.parent = parent

def find_next_node_in_inorder(node):
    if not node:
        return None

    # 有右子树
    if node.right:
        node = node.right
        while node:
            node = node.left
        return node

    # 没有右子树，有父亲节点
    if node.parent:
        parent = node.parent
        # 节点是父节点的左子节点，返回父节点
        if node == parent.left:
            return parent
        # 节点是父节点的右子节点，沿着父节点的指针一直向上，直到找到一个是它父节点的左子节点，如果有，返回这样的节点
        if node == parent.right:
            while parent.parent:
                if parent == parent.parent.left:
                    return parent
                parent = parent.parent
        return None

if __name__ == "__main__":
    node_i = TreeNode("i")
    node_h = TreeNode("h")
    node_g = TreeNode("g")
    node_f = TreeNode("f")
    node_e = TreeNode("e")
    node_d = TreeNode("d")
    node_c = TreeNode("c")
    node_b = TreeNode("b")
    node_a = TreeNode("a")
    set_relation(node_e, node_h, node_i)
    set_relation(node_c, node_f, node_g)
    set_relation(node_b, node_d, node_e)
    set_relation(node_a, node_b, node_c)

    print(find_next_node_in_inorder(node_i).data)
