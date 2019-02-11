#include "kth-greater-x-heap.h"

#include <vector>

int heap_compare(std::vector<int> heap, int index, int kth, int x) {
  if (index > heap.size() || kth <= 0)
    return kth;

  if (heap[index] < x) {
    kth = heap_compare(heap, (index << 1),     kth - 1, x);
    kth = heap_compare(heap, (index << 1) + 1, kth,     x);
  }

  return kth;
};