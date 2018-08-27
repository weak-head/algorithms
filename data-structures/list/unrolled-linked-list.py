
class Node:
    def __init__(self, max_size, next=None):
        self.el_num = 0
        self.elements = [None] * max_size
        self.next = next

class UnrolledLinkedList:
    def __init__(self, node_size):
        self._node_size = node_size
        self._head = Node(node_size, None)

    def append(self, data):
        node = self._head
        while node.next is not None:
            node = node.next

        if node.el_num == self._node_size:
            new_node = Node(self._node_size, node.next)
            node.next, node = new_node, new_node

        node.elements[node.el_num] = data
        node.el_num += 1

    def __str__(self):
        node, sr = self._head, ''
        while node is not None:
            sr += '['
            for i in range(0, node.el_num):
                sr += str(node.elements[i])
                sr += ',' if i != node.el_num - 1 else ']'
            node = node.next
            if node is not None:
                sr += ' -> '
        return sr

if __name__ == '__main__':
    lst = UnrolledLinkedList(4)

    for i in range(13):
        lst.append(i)

    print(lst)