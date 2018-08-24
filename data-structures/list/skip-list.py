'''
  Skip list implementation that uses recursion
  to backtrack the visited nodes to reduce the time
  of insertion and deletion.
'''

from random import randint

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class SkipList:
    def __init__(self, levels, probability):
        self._levels = levels
        self._p = probability
        self._sentinel = Node(None, [None] * self._levels)

    def insert(self, data):
        node = Node(data, [None] * self._levels)
        self.__insert(self._levels - 1, self._sentinel, node)

    def __insert(self, level, parent, node):
        # we are at the very bottom layer of our skip-list,
        # now we need to find the appropriate place to insert the node
        if (level == 0):
            el = parent
            while (el.next[level] is not None and node.data >= el.next[level].data):
                el = el.next[level]

            node.next[level] = el.next[level]
            el.next[level] = node

            return randint(1, self._p) == 1

        # the next node on this level has a bigger value,
        # we need to move one level down to find the right place
        if (parent.next[level] is None or node.data <= parent.next[level].data):
            add_link = self.__insert(level - 1, parent, node)

            if add_link:
                node.next[level] = parent.next[level]
                parent.next[level] = node
                return randint(1, self._p) == 1
            else:
                return False

        # move to the next node on this level
        return self.__insert(level, parent.next[level], node)

    def delete(self, data):
        self.__delete(data, self._levels - 1, self._sentinel)

    def __delete(self, data, level, parent):
        # the first element in our list is sentinel,
        # so we can safely we keep track of the next element in the chain,
        # without any additional checks
        if (level == 0):
            el = parent
            while (el.next[level] is not None and el.next[level].data != data):
                el = el.next[level]

            # delete the element from the bottom level
            if el.next[level] is not None:
                el.next[level] = el.next[level].next[level]

        elif (parent.next[level] is None or data <= parent.next[level].data):
            self.__delete(data, level - 1, parent)

            # re-adjust pointer on this level
            if (parent.next[level] is not None and parent.next[level].data == data):
                parent.next[level] = parent.next[level].next[level]

        else:
            self.__delete(data, level, parent.next[level])

    def find(self, data):
        el = self._sentinel
        for level in range(self._levels - 1, -1, -1):
            while (el.next[level] is not None and data > el.next[level].data):
                el = el.next[level]
            if (el.next[level] is not None and el.next[level].data == data):
                return data
        return None

    def rebalance(self):
        link, el, ptrs = True, self._sentinel, [self._sentinel] * self._levels
        while (el is not None):
            # remove all connections on all levels for this node
            # and possibly replace them with a new connections
            for level in range(1, self._levels):
                el.next[level] = None

                # create a new connection
                if (link and randint(1, self._p) == 1):
                    ptrs[level].next[level] = el
                    ptrs[level] = el
                else:
                    link = False

            el, link = el.next[0], True

    def __str__(self):
        res = ''
        for level in range(self._levels - 1, -1, -1):
            el, sr = self._sentinel.next[level], []
            while (el is not None):
                sr.append(str(el.data))
                el = el.next[level]
            res += str(level) + '| ' + ' -> '.join(sr) + '\n'
        return res


if __name__ == '__main__':
    ls = SkipList(4, 2)

    for i in range(20):
        ls.insert(randint(1, 40))
    print(ls)

    print('rebalance #1:')
    ls.rebalance()
    print(ls)

    print('rebalance #2:')
    ls.rebalance()
    print(ls)

    itm = None
    while itm != 0:
        itm = int(input('\ndel: '))
        ls.delete(itm)
        print(ls)

        itm = int(input('\nfind: '))
        fi = ls.find(itm)
        print(fi)

        print('rebalance:')
        ls.rebalance()
        print(ls)