'''
    Determine if k-th element of heap is less than X.
'''

from typing import List
from heapq import heapify

def nth_less(heap: List[int], head: int, element: int, k: int) -> int:
    if k == 0 or head >= len(heap):
        return k
    if heap[head] < element:
        k = nth_less(heap, left_child(head), element, k - 1)
        k = nth_less(heap, left_child(head) + 1, element, k)
    return k

def left_child(index: int) -> int:
    return (index << 1) + 1

if __name__ == '__main__':
    h = [67, 30, 22, 16, 15, 14, 9, 7, 5, 4, 1]
    heapify(h)

    # less than 20
    assert not nth_less(h, 0, 20, 1)
    assert not nth_less(h, 0, 20, 2)
    assert not nth_less(h, 0, 20, 3)
    assert not nth_less(h, 0, 20, 4)
    assert not nth_less(h, 0, 20, 5)
    assert not nth_less(h, 0, 20, 6)
    assert not nth_less(h, 0, 20, 7)
    assert not nth_less(h, 0, 20, 8)

    # greater than 20
    assert nth_less(h, 0, 20, 9)
    assert nth_less(h, 0, 20, 10)
    assert nth_less(h, 0, 20, 100)

    print('done')