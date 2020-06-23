class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    if not head:
        return None
    if not head.next:
        return head

    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


if __name__ == "__main__":
    l1_6 = Node(6)
    l1_5 = Node(5, l1_6)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head = l1_1
    p = reverse_list(head)
    while p:
        print(p.value)
        p = p.next