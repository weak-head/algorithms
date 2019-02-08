"""
    Detect loop in a linked list,
    without allocating any additional memory.
"""


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def mk_linked_loop():
    """
    Creates the linked list with a loop:
        1 -> 2 -> 3 -> 4 -> 5
                  ^         |
                   ---------
    """
    e5 = Node(5)
    e4 = Node(4, e5)
    e3 = Node(3, e4)
    e2 = Node(2, e3)
    e1 = Node(1, e2)
    e5.next = e3
    return e1

# O(n^2)
def has_loop(head: Node):
    if head is None:
        return False

    el, step = head.next, 1
    while el is not None:
        p, c = head, 0

        # searching for the current node,
        # (starting from the head) counting steps
        while p != el:
            p = p.next
            c += 1

        # the walked distance is not the same -> loop
        if c != step:
            return True
        else:
            el = el.next
            step += 1

    return False

if __name__ == '__main__':
    ll = mk_linked_loop()
    nl = Node(1, Node(2, Node(3, Node(4, Node(5)))))

    assert(has_loop(ll))
    assert(not has_loop(nl))