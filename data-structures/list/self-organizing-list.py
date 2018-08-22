
'''
Self-organizing list

    MTF:
        - adapts quickly
        - easy to destroy optimal ordering

    Count method:
        - closely reflects the actual access pattern
        - adapts slowly to the rapid changes in the access pattern

    Transpose method:
        - slow response to the changes in the access pattern
'''

class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

class SelfOrganizingList:
    '''Self Organizing list using Move-to-Front heuristic'''
    def __init__(self):
        self._head = None

    def add(self, data):
        item = Node(data, self._head)
        self._head = item

    def delete(self, data):
        if self.find(lambda d: d == data) is not None:
            self._head = self._head._next

    def find(self, predicate):
        p, c = None, self._head
        while (c is not None and not predicate(c._data)):
            p, c = c, c._next
        # Re-arrange based on MTF heuristic
        if c is not None and p is not None:
            p._next = c._next
            c._next = self._head
            self._head = c
        return c._data if c is not None else None

    def __str__(self):
        itm, sr = self._head, []
        while (itm is not None):
            sr.append(str(itm._data))
            itm = itm._next
        return ' -> '.join(sr)

if __name__ == '__main__':
    lst = SelfOrganizingList()

    lst.add(1)
    lst.add(2)
    lst.add(3)
    lst.add(4)
    print(str(lst))

    itm = lst.find(lambda n: n % 2 == 0)
    print('odd', itm, ' => ', str(lst))

    itm = lst.find(lambda n: n > 5)
    print('gt 5', itm, ' => ', str(lst))

    itm = lst.find(lambda n: n == 2)
    print('eq 2', itm, ' => ', str(lst))

    itm = lst.find(lambda n: n == 7)
    print('eq 7', itm, ' => ', str(lst))