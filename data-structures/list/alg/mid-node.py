class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def mid_node(head):
    el = mid = head
    while el.next is not None:
        el = el.next
        if el.next is not None:
            el  = el.next
            mid = mid.next
    return mid

def mk_list(collection):
    node = None
    for itm in reversed(collection):
        node = Node(itm, node)
    return node

if __name__ == '__main__':
    lst = mk_list([1,2,3,4,5,6,7,8,9,10])
    mid = mid_node(lst)
    print(mid.data)