class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delete_duplicated_node(head):
    if not head:
        return head

    new_head = Node(-1)
    start = new_head
    old_head = head
    dele_val = set()

    while head and head.next:
        if head.value == head.next.value:
            dele_val.add(head.value)
        head = head.next

    while old_head:
        if old_head.value not in dele_val:
            new_head.next = old_head
            new_head = old_head
        old_head = old_head.next

    return start.next

if __name__ == "__main__":
    l1_7 = Node(5)
    l1_6 = Node(4, l1_7)
    l1_5 = Node(4, l1_6)
    l1_4 = Node(3, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head = l1_1
    head_p = delete_duplicated_node(head)

    while head_p is not None:
        print(head_p.value)
        head_p = head_p.next
