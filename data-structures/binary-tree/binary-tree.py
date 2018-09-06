
'''
Unbalanced binary tree.
In the worst case could become pathological tree
(each parent node has only one associated child node).
'''

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    # O(h)
    def insert(self, data):
        if self._root is None:
            self._root = Node(data)
            return
        p, c = None, self._root
        while c is not None:
            p = c
            c = c.right if data > c.data else c.left
        if data > p.data:
            p.right = Node(data)
        else:
            p.left = Node(data)

    # O(h)
    def find(self, data):
        return BinaryTree.__find(self._root, data)

    @staticmethod
    def __find(node, data):
        if node is None or node.data == data:
            return node
        elif data > node.data:
            return BinaryTree.__find(node.right, data)
        else:
            return BinaryTree.__find(node.left, data)

    # O(h)
    def delete(self, data):
        # node = BinaryTree.__find(self._root, data)
        pass

    # O(n)
    def traverse(self, f):
        BinaryTree.__traverse(self._root, f)

    @staticmethod
    def __traverse(node, f):
        if node is None:
            return
        BinaryTree.__traverse(node.left, f)
        f(node.data)
        BinaryTree.__traverse(node.right, f)


if __name__ == '__main__':
    tree = BinaryTree()

    tree.insert(4)
    tree.insert(2)
    tree.insert(6)

    tree.traverse(print)
    print()

    tree.insert(1)
    tree.insert(3)
    tree.insert(7)
    tree.insert(5)

    tree.traverse(print)
    print()

    n = tree.find(6)
    print(n.data)