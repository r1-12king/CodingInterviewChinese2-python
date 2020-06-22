class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next




def delete_node(head, p):
    """
    题目一：O(1)时间内删除链表节点
    前提：要删除的节点要在链表里面
    """
    if not head or not p:
        return head

    # 只有一个节点
    if head == p or p.next == None:
        head = None
        return head

    # 删除的是尾结点
    if p.next == None:
        q = head
        while q.next!=p:
            q = q.next
        q.next = None
        return head

    # 一般结点
    next_node = p.next
    p.value = next_node.value
    p.next = next_node.next
    return head


if __name__ == '__main__':
    l1_5 = Node(10)
    l1_4 = Node(7, l1_5)
    l1_3 = Node(5, l1_4)
    l1_2 = Node(2, l1_3)
    l1_1 = Node(1, l1_2)
    head_p = delete_node(l1_1, l1_2)

    while head_p is not None:
        print(head_p.value)
        head_p = head_p.next

