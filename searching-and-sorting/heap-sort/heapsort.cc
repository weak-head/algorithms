#include <iostream>
#include <vector>

typedef std::vector<int> Array;

void Heapify(Array array, int index) {
  if (index > array.size())
    return;

  int lchild_ix = index << 1;
  int rchild_ix = lchild_ix + 1;
  int min_index = index;

  if (lchild_ix <= array.size())
    min_index = (array[min_index] < array[lchild_ix]) ? min_index : lchild_ix;

  if (rchild_ix <= array.size())
    min_index = (array[min_index] < array[rchild_ix]) ? min_index : rchild_ix;

  if (min_index != index) {
    std::swap(array[index], array[min_index]);
    Heapify(array, min_index);
  }
}

// O (log n)
Array BuildPriorityQueue(Array array) {
  Array priorityQueue(array);

  for (int i = (priorityQueue.size() >> 1); i >= 0; i--) {
    Heapify(priorityQueue, i);
  }

  return priorityQueue;
}

// O (n * log n)
void Heapsort(Array array) {
  Array priority_queue = BuildPriorityQueue(array);


}

int main() {

}