class TreeNode(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 返回对应节点TreeNode
#中序遍历，得到一个递增数列
def KthNode(pRoot, k):
    # write code here
    if not pRoot:
        return None
    if k<=0:
        return
    count = 0
    stack = []
    root = pRoot
    while stack or root:
        #节点不空，不断加左节点
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        count += 1
        if count == k:
            return root
        root = root.right



if __name__ == "__main__":
    node8 = TreeNode(8)
    node6 = TreeNode(6)
    node4 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(3, node2, node4)
    node7 = TreeNode(7, node6, node8)
    node5 = TreeNode(5, node3, node7)
    root = node5

    res = KthNode(root,3)
    print(res.value)