class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_loop(head):
    """
    判断一个链表是否有环，有的话返回环中的节点个数
    """
    if not head:
        return 0

    p1 = head
    p2 = head

    while True:
        for _ in range(2):
            if not p1.next:
                return 0
            p1 = p1.next
        p2 = p2.next
        if p1 == p2:
            break

    num_of_loop = 0
    while True:
        p1 = p1.next
        num_of_loop+=1
        if p1 == p2:
            break

    return num_of_loop


def findEntryOfLoop(head):
    num_of_loop = find_loop(head)
    if num_of_loop == 0:
        return None
    p1 = head
    p2 = head
    while num_of_loop:
        p1 = p1.next
        num_of_loop -= 1
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1

if __name__ == "__main__":
    l1_6 = Node(6)
    l1_5 = Node(5, l1_6)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    l1_6.next = l1_5
    head = l1_1
    print(findEntryOfLoop(head).value)