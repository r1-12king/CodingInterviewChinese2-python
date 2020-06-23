class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_list(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    phead = None

    if l1.value < l2.value:
        phead = l1
        phead.next = merge_list(l1.next,l2)
    else:
        phead = l2
        phead.next = merge_list(l1,l2.next)


    return phead


if __name__ == "__main__":
    l1_5 = Node(10)
    l1_4 = Node(7, l1_5)
    l1_3 = Node(5, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)

    l2_3 = Node(6)
    l2_2 = Node(6, l2_3)
    l2_1 = Node(5, l2_2)
    l1_1 = merge_list(l1_1, l2_1)

    while l1_1 is not None:
        print(l1_1.value)
        l1_1 = l1_1.next