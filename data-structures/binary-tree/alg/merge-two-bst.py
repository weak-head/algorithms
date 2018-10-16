#
# Merge two BST
#
# All elements in the first BST
# should be less than elements in the second BST
#

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self._head = None

    # O(h)
    def insert(self, data):
        if self._head is None:
            self._head = Node(data)
        else:
            parent, el = None, self._head
            while (el is not None):
                parent = el
                el = el.left if data < el.data else el.right
            if data < parent.data:
                parent.left = Node(data)
            else:
                parent.right = Node(data)

    # O(h)
    def merge(self, bst):
        parent, self_max = None, self._head
        while (self_max.right is not None):
            parent   = self_max
            self_max = self_max.right
        if parent is not None:
            parent.right = self_max.left
        self_max.left  = self._head
        self_max.right = bst._head
        self._head     = self_max

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

    bst_gt = BST()
    items = [1000, 500, 2000, 450, 650, 2700]
    for i in items:
        bst_gt.insert(i)

    print('-----')
    print('fist:')
    bst.traverse(print)

    print('-----')
    print('second:')
    bst_gt.traverse(print)

    print('-----')
    print('merged:')
    bst.merge(bst_gt)
    bst.traverse(print)