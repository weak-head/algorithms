'''
    Least Recently Used Cache
    https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
'''

class LRUCache:
    class DLinkNode:
        def __init__(self, key: int, value: int, prev = None, next = None):
            self.prev  = prev
            self.next  = next
            self.key   = key
            self.value = value

    def __init__(self, capacity: int):
        self._keymap    = {}
        self._capacity  = capacity
        self._count     = 0
        self._head      = self.DLinkNode(None, None)
        self._tail      = self.DLinkNode(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        if key not in self._keymap:
            return -1
        node = self._keymap[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        pass

    def _move_to_front(self, node: LRUCache.DLinkNode):
        '''
            Move the node to the front of the doubly linked list.
            O(1)
        '''
        # detach node
        node.prev.next = node.next
        node.next.prev = node.prev
        # attach to head
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node

if __name__ == '__main__':
    cache = LRUCache(5)