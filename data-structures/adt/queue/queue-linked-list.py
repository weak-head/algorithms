
class Item:
    def __init__(self, data, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next

class Queue:
    def __init__(self):
        self._sentinel = Item(None)
        self._sentinel._next = self._sentinel
        self._sentinel._prev = self._sentinel

    def enqueue(self, data):
        item = Item(data, self._sentinel, self._sentinel._next)
        self._sentinel._next._prev = item
        self._sentinel._next = item

    def dequeue(self):
        ret = self._sentinel._prev
        if ret == self._sentinel:
            return None
        else:
            self._sentinel._prev = ret._prev
            ret._prev._next = self._sentinel
            return ret._data

    def peek(self):
        return self._sentinel._prev._data if self._sentinel._prev != self._sentinel else None

    def __str__(self):
        rep, el = [], self._sentinel._next
        while el != self._sentinel:
            rep.append(str(el._data))
            rep.append(' |-> ')
            el = el._next
        return ''.join(rep)

def test_case():
    que = Queue()

    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)

    print(str(que))

    i1 = que.dequeue()
    i2 = que.dequeue()

    print('dequeue: {itm}'.format(itm=i1))
    print('dequeue: {itm}'.format(itm=i2))
    print(str(que))

    i3 = que.peek()
    i4 = que.peek()

    print('peek: {itm}'.format(itm=i3))
    print('peek: {itm}'.format(itm=i4))
    print(str(que))

if __name__ == '__main__':
    test_case()