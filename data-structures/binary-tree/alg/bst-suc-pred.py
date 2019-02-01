#!/usr/bin/python3

# O(1) successor and predecessor in BST
# - BST with embedded doubly linked list -

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
                parent.right = Node(data, pred=parent, suc=parent.suc)
                if parent.suc is not None:
                    parent.suc.pred = parent.right
                parent.suc = parent.right
            else:
                self._insert(parent.right, data)
        else:
            if parent.left is None:
                parent.left = Node(data, suc=parent, pred=parent.pred)
                if parent.pred is not None:
                    parent.pred.suc = parent.left
                parent.pred = parent.left
            else:
                self._insert(parent.left, data)

    def min(self):
        def _min(node):
            if node.left is None:
                return node
            else:
                return _min(node.left)
        if self._head is None:
            return None
        else:
            return _min(self._head)

    def max(self):
        def _max(node):
            if node.right is None:
                return node
            else:
                return _max(node.right)
        if self._head is None:
            return None
        else:
            return _max(self._head)

    def traverse(self, f):
        def _traverse(node, f):
            if node is None:
                return
            _traverse(node.left, f)
            f(node.data)
            _traverse(node.right, f)
        _traverse(self._head, f)

def successor(node):
    return node.suc

def predecessor(node):
    return node.pred

if __name__ == '__main__':
    bst = BST()

    items = [100, 50, 200, 25, 70, 150, 250, 5, 30, 60, 80, 180, 75, 90]
    for i in items:
        bst.insert(i)

    print('The BST:')
    bst.traverse(print)
    print('\n')

    print('min to max:')
    element = bst.min()
    while element is not None:
        print(element.data)
        element = successor(element)
    print('\n')

    print('max to min:')
    element = bst.max()
    while element is not None:
        print(element.data)
        element = predecessor(element)
    print('\n')