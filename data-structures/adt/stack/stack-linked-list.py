
class Frame:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

class Stack:
    def __init__(self):
        self._head = None

    def push(self, data):
        self._head = Frame(data, self._head)

    def pop(self):
        if self._head is None:
            return None

        data       = self._head._data
        self._head = self._head._next
        return data

    def peek(self):
        return self._head._data if self._head is not None else None

    def __str__(self):
        rep, el = [], self._head
        while el is not None:
            rep.append(' -> ')
            rep.append(str(el._data))
            el = el._next

        return ''.join(rep)

def test_case():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print( str(stack) )

    p1 = stack.pop()
    p2 = stack.pop()

    print('pop: {itm}'.format(itm=p1))
    print('pop: {itm}'.format(itm=p2))
    print( str(stack) )

    p3 = stack.peek()
    p4 = stack.peek()

    print('peek: {itm}'.format(itm=p3))
    print('peek: {itm}'.format(itm=p4))
    print( str(stack) )

if __name__ == '__main__':
    test_case()