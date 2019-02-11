#include "kth-greater-x-heap.h"

#include <vector>

/*
  Problem:
    Determine whether the k-th smallest element in the heap,
    is great than or equal to x.

  Inefficient solutions:
    K calls to extract min -> O(k * log n)
    Check all nodes up to k deepth -> O(min(n, 2^k))

  Efficient solution:
    Look only at k elements smaller than x -> O(k)
*/
int heap_compare(std::vector<int> heap, int index, int count, int x) {
  if (index > heap.size() || count <= 0)
    return count;

  if (heap[index] < x) {
    count = heap_compare(heap, (index << 1),     count - 1, x);
    count = heap_compare(heap, (index << 1) + 1, count,     x);
  }

  return count;
};