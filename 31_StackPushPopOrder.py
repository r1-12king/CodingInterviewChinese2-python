def is_pop_order(inorder, outorder):
    if not inorder or not outorder :
        return False

    if len(inorder) != len(outorder) or set(inorder) != set(outorder):
        return False


    stack = []

    for i in outorder:
        while len(stack) == 0 or i != stack[-1]:
            if len(inorder)==0:
                return False
            stack.append(inorder.pop(0))
        stack.pop()

    return True


if __name__ == '__main__':
    res = is_pop_order([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    print(res)
    res = is_pop_order([1, 2, 3, 4, 5], [3, 5, 4, 1, 2])
    print(res)
