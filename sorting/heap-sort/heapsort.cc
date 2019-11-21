#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <iterator>
#include <functional>

typedef std::vector<int> Array;
typedef std::vector<int> PriorityQueue;

using namespace std;

// O(log n)
void Heapify(PriorityQueue& pq, int index) {
  if (index >= pq.size())
    return;

  int lchild_ix = index << 1;
  int rchild_ix = lchild_ix + 1;
  int min_index = index;

  if (lchild_ix < pq.size())
    min_index = (pq[min_index] < pq[lchild_ix]) ? min_index : lchild_ix;

  if (rchild_ix < pq.size())
    min_index = (pq[min_index] < pq[rchild_ix]) ? min_index : rchild_ix;

  if (min_index != index) {
    std::swap(pq[index], pq[min_index]);
    Heapify(pq, min_index);
  }
}

// O(log n)
PriorityQueue BuildPriorityQueue(const Array& array) {
  PriorityQueue priorityQueue(array);

  for (int i = (priorityQueue.size() >> 1); i >= 0; i--)
    Heapify(priorityQueue, i);

  return priorityQueue;
}

// O(log n)
int ExtractMin(PriorityQueue& pq) {
  int min = pq[0];

  pq[0]   = pq[pq.size() - 1];
  pq.pop_back();

  Heapify(pq, 0);

  return min;
}

/*
  The heapsort could be seen as greatly improved version
  of the selection sort that takes adventage of the priority queue.

  It takes O(log n) to build a priority queue and O(log n)
  to extract a top element from the queue.

  The total running time is O(n * log n).

  One downside of heapsort is that it requires O(n) additional space
  for the priority queue.
*/
void Heapsort(Array& array) {
  PriorityQueue priority_queue = BuildPriorityQueue(array);

  for (int i = 0; i < array.size(); i++)
    array[i] = ExtractMin(priority_queue);
}

Array GenerateRandomArray() {
  random_device rnd_device;
  mt19937 mersenne_engine { rnd_device() };
  uniform_int_distribution<int> dist {1, 100};

  auto gen =
    [&dist, &mersenne_engine]() {
      return dist(mersenne_engine);
    };

  vector<int> vec(13);
  generate(begin(vec), end(vec), gen);

  return vec;
}

int main() {
  Array array = GenerateRandomArray();
  Heapsort(array);

  for (auto i : array)
    cout << i << " ";

  cout << endl;
}