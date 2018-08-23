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

    print(str(ls))
