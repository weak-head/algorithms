
class Node:
    def __init__(self, data, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next

class Dequeue:
    def __init__(self):
        self._sentinel = Node(None)
        self._sentinel._prev = self._sentinel
        self._sentinel._next = self._sentinel

    def __str__(self):
        el, rep = self._sentinel._next, []

        while (el != self._sentinel):
            rep.append(str(el._data))
            el = el._next

        return ' -> '.join(rep)

    def append(self, data):
        node = Node(data, self._sentinel._prev, self._sentinel)
        self._sentinel._prev._next = node
        self._sentinel._prev = node

    def appendleft(self, data):
        node = Node(data, self._sentinel, self._sentinel._next)
        self._sentinel._next._prev = node
        self._sentinel._next = node

    def pop(self):
        node = self._sentinel._prev
        self._sentinel._prev._prev._next = self._sentinel._prev._next
        return node._data if node != self._sentinel else None

    def popleft(self):
        node = self._sentinel._next
        self._sentinel._next._next._prev = self._sentinel._next._prev
        return node._data if node != self._sentinel else None


if __name__ == '__main__':
    dq = Dequeue()

    itm1 = dq.pop()
    itm2 = dq.popleft()

    print('pop: {itm}'.format(itm=itm1))
    print('popleft: {itm}'.format(itm=itm2))

    dq.append(1)
    dq.append(2)
    dq.append(3)

    dq.appendleft(40)
    dq.appendleft(50)
    dq.appendleft(60)

    print(str(dq))

    itm1 = dq.pop()
    itm2 = dq.popleft()

    print('pop: {itm}'.format(itm=itm1))
    print('popleft: {itm}'.format(itm=itm2))
    print(str(dq))