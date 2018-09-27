
'''
Fixed size hash table that uses separate chaining for hash collision resolution.
The hash table and the hash function itself are designed to work with ASCII strings.
'''

class Hashtable:
    def __init__(self, capacity):
        self._capacity = capacity
        self._map = [[] for x in range (capacity)]

    def insert(self, key,  value):
        index = self.__get_index(key)
        self._map[index].append((key, value))

    # worst case O(n), expected O(1)
    def remove(self, key):
        index = self.__get_index(key)
        for ix, (k, _) in enumerate(self._map[index]):
            if key == k:
               del self._map[index][ix]
               break

    # worst case O(n), expected O(1)
    def contains(self, key):
        index = self.__get_index(key)
        for (k, _) in self._map[index]:
            if key == k:
                return True
        return False

    def __get_index(self, str_object):
        return Hashtable.get_hash(str_object) % self._capacity

    def __str__(self):
        srep = '<---->\n'
        for ix, bucket in enumerate(self._map):
            srep += str(ix) + ' -> ' + str(bucket) + '\n'
        srep += '<---->\n'
        return srep

    # O(k), where k is the length of the string
    @staticmethod
    def get_hash(str_object):
        hash = 0
        for index, char in enumerate(str_object):
            hash += (255 ^ index) * ord(char)
        return hash

if __name__ == '__main__':
    h = Hashtable(7)
    print(h)
    print('contains "abc":', h.contains('abc'), '\n')

    h.insert('abc', 1)
    h.insert('abb', 2)
    h.insert('aba', 3)
    h.insert('f', 4)
    h.insert('zz', 5)
    h.insert('zfa', 6)
    print(h)
    print('contains "abc":', h.contains('abc'), '\n')

    h.remove('zfa')
    print(h)

    h.remove('abc')
    print(h)
    print('contains "abc":', h.contains('abc'), '\n')