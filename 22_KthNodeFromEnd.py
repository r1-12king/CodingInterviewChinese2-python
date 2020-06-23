class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def findKthToTail(head, k):
    if not head or k == 0:
        return None

    p1 = head
    p2 = head
    index = k-1

    while p1 and k-1:
        p1 = p1.next
        k = k-1
        if not p1:
            return None


    while p1.next:
        p1 = p1.next
        p2 = p2.next

    return p2

if __name__ == "__main__":
    l1_5 = Node(5)
    l1_4 = Node(4, l1_5)
    l1_3 = Node(3, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head = l1_1
    res = findKthToTail(head, 7)
    if res:
        print(res.value)
    print(res)