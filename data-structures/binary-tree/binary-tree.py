
'''
Unbalanced binary tree.
In the worst case could become pathological tree
(each parent node has only one associated child node).
'''

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


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
            p.right = Node(data, p)
        else:
            p.left = Node(data, p)

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
        node = BinaryTree.__find(self._root, data)
        new_child = None

        # 0 children
        if node.left is None and node.right is None:
            pass
        # 2 children
        elif node.left is not None and node.right is not None:
            new_child = node.left
            max_child = new_child
            while max_child.right is not None:
                max_child = max_child.right
            max_child.right = node.right
            node.right.parent = max_child
        # 1 child
        else:
            new_child = node.left if node.left is not None else node.right
            new_child.parent = node.parent

        # root
        if node.parent is None:
            self._root = new_child
        # left child
        elif node.parent.left == node:
            node.parent.left = new_child
        # right child
        else:
            node.parent.right = new_child

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
    print()

    tree.delete(1)
    tree.delete(4)
    tree.delete(5)
    tree.traverse(print)