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
        self._insert(self._levels, self._sentinel, node)

    def _insert(self, level, parent, node):
        if (level == 1):
            el = parent
            while (el.next[level] is not None and node.data <= el.next[level].data):
                el = el.next[level]

            node.next[level] = el.next[level]
            el.next[level] = node

            return randint(1, self._p) == 1

        if (parent.next[level] is None or node.data <= parent.next[level].data):
            # move one level down on the same node
            add_link = self._insert(level - 1, parent, node)

            if add_link:
                node.next[level] = parent.next[level]
                parent.next[level] = node
                return randint(1, self._p) == 1
            else:
                return False

        # move to the next node on this level
        return self._insert(level, parent.next[level], node)

