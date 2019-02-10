#ifndef HEAP_H_
#define HEAP_H_

#include <vector>

template<typename T>
class Heap {
 public:
  Heap();
  ~Heap();

  void Insert(T item);

  T Min();
  T ExtractMin();

  int Size() const { return size_; };

 private:
  void heapify(int index);
  void bubble_up(int index);
  int parent(int index);
  int young_child(int index);

  std::vector<T> vec_;
  int size_;
};

#endif