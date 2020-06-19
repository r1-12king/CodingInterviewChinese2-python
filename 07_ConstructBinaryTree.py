class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1],inorder[:mid])
    root.right = buildTree(preorder[mid+1:],inorder[mid+1:])
    return root

def print_level(node, position_name):
    if node is None:
        return
    print_level(node.left, "left")
    print_level(node.right, "right")
    print()
    print(position_name, " ", node.data, end=' ')

if __name__ == "__main__":
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    root = buildTree(preorder=preorder, inorder=inorder)
    print_level(root, "root")