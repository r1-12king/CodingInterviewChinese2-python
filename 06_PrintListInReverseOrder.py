class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_list_reverse_with_stack(head):
    """
    用栈实现，鲁棒性好
    """
    stack = []
    while head:
        stack.append(head.data)
        head = head.next

    while stack:
        print(stack.pop())


def print_list_reverse_with_recursion(head):
    """
    用递归实现，可能导致函数调用栈溢出
    """
    if not head:
        return
    print_list_reverse_with_recursion(head.next)
    print(head.data)


if __name__ == '__main__':
    n5 = Node(data=5)
    n4 = Node(data=4, next=n5)
    n3 = Node(data=3, next=n4)
    n2 = Node(data=2, next=n3)
    head = Node(data=1, next=n2)
    print_list_reverse_with_stack(head)
    print("-------------------------")
    print_list_reverse_with_recursion(head)