
# N-th min element in BST.

class Node:
    def __init__(self, data, left=None, right=None, cleft=0):
        self.data  = data
        self.left  = left
        self.right = right
        self.cleft = cleft

class BST:
    def __init__(self):
        self._head = None

    # O(h)
    def insert(self, data):
        if self._head is None:
            self._head = Node(data)
        else:
            self.__backtrack_insert(self._head, data)

    def __backtrack_insert(self, parent_node, data):
        if data <= parent_node.data:
            if parent_node.left is not None:
                self.__backtrack_insert(parent_node.left, data)
                parent_node.cleft += 1
            else:
                parent_node.left = Node(data)
                parent_node.cleft = 1
        else:
            if parent_node.right is not None:
                self.__backtrack_insert(parent_node.right, data)
            else:
                parent_node.right = Node(data)

    # O(h)
    def min(self, nth):
        node = self._head
        ix   = node.cleft + 1

        while (ix != nth and node is not None):
            if nth < ix:
                parent_cleft = node.cleft
                node = node.left
                ix   = ix - (parent_cleft - node.cleft)
            else:
                node = node.right
                ix   = ix + node.cleft + 1

        return node.data if node is not None else None

if __name__ == '__main__':
    bst = BST()
    items = [100, 50, 200, 25, 70, 150, 250, 5, 30, 60, 80, 180, 75, 90]
    for itm in items:
        bst.insert(itm)

    for i in range(1, len(items)):
        print(i, ' -> ', bst.min(i))