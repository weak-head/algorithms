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
        if capacity == 0:
            raise Exception('Capacity cannot be zero')
        self._keymap    = {}
        self._capacity  = capacity
        self._count     = 0
        self._head      = self.DLinkNode(None, None)
        self._tail      = self.DLinkNode(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        '''
            Get value from LRU Cache
            O(1)
        '''
        if key not in self._keymap:
            return -1
        node = self._keymap[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        '''
            Put value into LRU Cache
            O(1)
        '''
        # the key/value is in the cache,
        # we only need to move it to front of DList
        if key in self._keymap:
            node = self._keymap[key]
            node.value = value
            self._move_to_front(node)
        # the key/value is not in the cache
        else:
            if self._count < self._capacity:
                node = self.DLinkNode(key, value)
                self._move_to_front(node, detach = False)
                self._keymap[key] = node
                self._count += 1
            # cache is full
            else:
                lru_node = self._tail.prev
                del self._keymap[lru_node.key]
                lru_node.key   = key
                lru_node.value = value
                self._move_to_front(lru_node)
                self._keymap[key] = lru_node

    def _move_to_front(self, node: DLinkNode, detach: bool = True):
        '''
            Move the node to the front of the doubly linked list.
            O(1)
        '''
        # detach node
        if detach:
            node.prev.next = node.next
            node.next.prev = node.prev
        # attach to head
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node

if __name__ == '__main__':
    cache = LRUCache(5)