#!/usr/bin/python3

# O(1) successor and predecessor in BST

class Node:
    def __init__(self, data, left=None, right=None, suc=None, pred=None):
        self.left  = left
        self.right = right
        self.suc   = suc
        self.pred  = pred
        self.data  = data

class BST:
    def __init__(self):
        self._head = None

    def insert(self, data):
        if self._head is None:
            self._head = Node(data)
        else:
            self._insert(self._head, data)

    def _insert(self, parent, data):
        if parent.data < data:
            if parent.right is None:
                parent.right = Node(data, pred=parent)
                parent.suc   = parent.right
            else:
                self._insert(parent.right, data)
        else:
            if parent.left is None:
                parent.left = Node(data, suc=parent)
                parent.pred = parent.left
            else:
                self._insert(parent.left, data)

    def traverse(self, f):
        def _traverse(node, f):
            if node is None:
                return
            _traverse(node.left, f)
            f(node.data)
            _traverse(node.right, f)
        _traverse(self._head, f)


if __name__ == '__main__':
    bst = BST()

    items = [100, 50, 200, 25, 70, 150, 250, 5, 30, 60, 80, 180, 75, 90]
    for i in items:
        bst.insert(i)

    bst.traverse(print)