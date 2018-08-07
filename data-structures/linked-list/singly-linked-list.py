
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class List:
    def __init__(self):
        self._head = None


    def __str__(self):
        rep = []

        itm = self._head
        while itm is not None:
            rep.append(str(itm.data))
            itm = itm.next

        rep = list( ','.join(rep) )
        rep.insert(0, '[')
        rep.append(']')

        return ''.join(rep)


    def prepend(self, item):
        node = Node(item, self._head)
        self._head = node


    def append(self, item):
        node = Node(item)

        if self._head is None:
            self._head = node
            return

        last = self._head
        while last.next is not None:
            last = last.next

        last.next = node


    def insert(self, index, item):
        node = Node(item)

        if self._head is None:
            self._head = node
            return

        if index == 0:
            node.next = self._head
            self._head = node
            return

        ix, el = index, self._head
        while (ix > 1) and (el.next is not None):
            el, ix = el.next, ix - 1

        node.next = el.next
        el.next = node


    def delete(self, item):
        if self._head is None:
            return

        if self._head.data == item:
            self._head = self._head.next
            return

        match = self._head
        while (match.next is not None) and (match.next.data != item):
            match = match.next

        match.next = match.next.next


    def find(self, item):
        ix, el = 0, self._head

        while (el is not None) and (el.data != item):
            ix, el = ix + 1, el.next

        return ix if el else None


def test_case():

    lst = List() # []

    lst.append(1) # [1]
    lst.append(2) # [1,2]
    lst.append(3) # [1,2,3]

    lst.prepend(0) # [0,1,2,3]
    lst.prepend(42) # [42,0,1,2,3]

    lst.insert(0, 40) # [40,42,0,1,2,3]
    lst.insert(100, 4) # [40,42,0,1,2,3,4]
    lst.insert(2, 43) # [40,42,43,0,1,2,3,4]
    lst.insert(1, 41) # [40,41,42,43,0,1,2,3,4]

    print( str(lst) )

    lst.delete(40) # [41,42,43,0,1,2,3,4]
    lst.delete(4) # [41,42,43,0,1,2,3]
    lst.delete(0) # [41,42,43,1,2,3]

    print( str(lst) )

    print( lst.find(41) ) # 0
    print( lst.find(3) ) # 5
    print( lst.find(1) ) # 3
    print( lst.find(143) ) # None


if __name__ == '__main__':
    test_case()