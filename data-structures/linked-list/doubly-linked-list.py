from itertools import chain, repeat, islice

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class List:
    def __init__(self):
        self._sentinel = Node(data=None)
        self._sentinel.next = self._sentinel
        self._sentinel.prev = self._sentinel

    def __str__(self):
        rep, ix = [], self._sentinel.next
        while (ix != self._sentinel):
            rep.append( str(ix.data) )
            ix = ix.next
        rep = list(intersperse(',', rep))
        rep.insert(0, '[')
        rep.append(']')
        return ''.join(rep)

    def append(self, item):
        node = Node(item, self._sentinel, self._sentinel.prev)
        self._sentinel.prev.next = node
        self._sentinel.prev = node

    def prepend(self, item):
        node = Node(item, self._sentinel.next, self._sentinel)
        self._sentinel.next.prev = node
        self._sentinel.next = node

    def delete(self, item):
        ix = self._sentinel.next
        while (ix != self._sentinel) and (ix.data != item):
            ix = ix.next
        if (ix.data == item):
            ix.prev.next, ix.next.prev = ix.next, ix.prev

    def insert(self, index, item):
        ix, el = index, self._sentinel.next
        while (ix > 0) and (el != self._sentinel):
            el = el.next
        node = Node(item, el, el.prev)
        el.prev.next = node
        el.prev = node

    def search(self, predicate):
        el = self._sentinel.next
        while (el != self._sentinel) and (not predicate(el.data)):
            el = el.next
        return el.data if el != self._sentinel else None


def intersperse(delimiter, seq):
    return islice(chain.from_iterable(zip(repeat(delimiter), seq)), 1, None)


if __name__ == '__main__':
    lst = List()

    lst.append(1)
    lst.append(2)
    lst.append(3)

    lst.prepend(0)
    lst.prepend(42)

    print( str(lst) )

    lst.delete(2)
    lst.delete(42)
    lst.delete(3)
    lst.delete(120)

    print( str(lst) )

    lst.insert(0, 44)
    lst.insert(3, 2)
    lst.insert(100, 3)

    print (str(lst))

    r1 = lst.search(lambda x: x == 2)
    r2 = lst.search(lambda x: x % 2 == 1)
    r3 = lst.search(lambda x: x > 400)

    print('eq 2 => {itm}'.format(itm=r1))
    print('odd => {itm}'.format(itm=r2))
    print('gt 400 => {itm}'.format(itm=r3))