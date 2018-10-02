class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reversed(el):
    new_head = None
    while el is not None:
        new_head = Node(el.data, new_head)
        el = el.next
    return new_head

def traverse(el, f):
    while el is not None:
        f(el.data)
        el = el.next

if __name__ == '__main__':
    ls = Node(1, Node(2, Node(3, Node(4, None))))
    traverse(ls, print); print()

    lsr = reversed(ls)
    traverse(lsr, print)