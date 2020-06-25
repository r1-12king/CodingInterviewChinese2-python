class ComplexNode(object):
    def __init__(self, value, next=None, sibling=None):
        self.value = value
        self.next = next
        self.sibling = sibling

def copy_nodes(head):
    p = head
    while p:
        copy_node = ComplexNode(p.value)
        copy_node.next = p.next
        p.next = copy_node
        p = copy_node.next

def set_sibling(head):
    p = head
    while p:
        p_copy = p.next
        if p.sibling:
            p_copy.sibling = p.sibling.next
        p = p_copy.next

def reconnect_nodes(head):
    p = head
    p_copy = None
    p_copy_head = None

    if p:
        p_copy = p_copy_head = p.next
        p.next = p_copy.next
        p = p.next

    while p:
        p_copy.next = p.next
        p_copy = p_copy.next
        p.next = p_copy.next
        p = p.next



    return p_copy_head


def copy_complex_link(head):
    if not head:
        return None

    copy_nodes(head)
    set_sibling(head)
    return reconnect_nodes(head)


def display(head):
    if not isinstance(head, ComplexNode):
        return
    p = head
    while p:
        print(p.value, end=" ")
        if p.next:
            print(p.next.value, end=" ")
        if p.sibling:
            print(p.sibling.value, end=" ")
        print()
        p = p.next


if __name__ == "__main__":
    node5 = ComplexNode('E')
    node4 = ComplexNode('D', next=node5)
    node3 = ComplexNode('C', next=node4)
    node2 = ComplexNode('B', next=node3)
    node1 = ComplexNode('A', next=node2)
    node1.sibling = node3
    node2.sibling = node5
    node4.sibling = node2
    head = node1
    clone_head = copy_complex_link(head)
    display(head)
    print()
    display(clone_head)
