'''
Fixed size hash table that uses open addressing (linear probing) for hash collision resolution.
'''

class Hashtable:
    def __init__(self, capacity):
        self._map = [None] * capacity
        self._capacity = capacity

    # depends on load factor and hash distribution quality. Expected O(1), worst case O(n)
    def insert(self, key, value):
        index = self.__find_slot(key)
        if index is None:
            raise Exception('Fully loaded hash-table')
        self._map[index] = (key, value)

    # O(n), for fully loaded table
    def __find_slot(self, key):
        index = self.__get_index(key)
        base_index = index
        while (self._map[index] is not None) and (self._map[index][0] != key):
            index = (index + 1) % self._capacity
            # fully loaded hash table
            if index == base_index:
                break
        return index if self._map[index] is None or self._map[index][0] == key else None

    def __get_index(self, key):
        return Hashtable.__get_hash(key) % self._capacity

    def __str__(self):
        srep = '<---->\n'
        for ix, slot in enumerate(self._map):
            srep += str(ix) + ' -> ' + str(slot) + '\n'
        srep += '<---->\n'
        return srep

    @staticmethod
    def __get_hash(string_object):
        hash = 0
        for ix, c in enumerate(string_object):
            hash += (255 ^ ix) * ord(c)
        return hash


if __name__ == '__main__':
    ht = Hashtable(3)

    ht.insert('abc', 1)
    ht.insert('gas', 2)
    ht.insert('zzz', 3)
    print(ht)

    ht.insert('faf', 4)
    print(ht)