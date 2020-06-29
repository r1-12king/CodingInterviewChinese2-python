class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_first_commom_node_1(head1, head2):
    """
    时间：O(m+n)
    """
    if not head1 or not head2:
        return None

    len1 = get_length(head1)
    len2 = get_length(head2)

    if len1 > len2:
        longHead = head1
        shortHead = head2
        nLenDif = len1 - len2
    else:
        longHead = head2
        shortHead = head1
        nLenDif = len2 - len1

    for i in range(nLenDif):
        longHead = longHead.next

    while longHead and shortHead:
        if longHead == shortHead:
            return longHead.value
        longHead = longHead.next
        shortHead = shortHead.next

    return None


def get_length(head):
    count = 0
    p = head
    while p:
        count += 1
        p = p.next
    return count


def find_first_commom_node_2(head1, head2):
    """
    用set
    """
    if not head1 or not head2:
        return None

    sets = set()
    while head1:
        sets.add(head1)
        head1 = head1.next
    while head2:
        if head2 in sets:
            return head2.value
        head2 = head2.next
    return None


if __name__ == "__main__":
    node7 = Node(7)
    node6 = Node(6, node7)
    node5 = Node(5, node6)
    node4 = Node(4, node5)
    head2 = node4

    node3 = Node(3, node6)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    head1 = node1
    print(find_first_commom_node_1(head1, head2))
    print(find_first_commom_node_2(head1, head2))
