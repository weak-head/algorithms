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
            ix.prev, ix.next = ix.next, ix.prev


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