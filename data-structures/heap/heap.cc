#include "heap.h"
#include <iostream>

template<typename T>
Heap<T>::Heap() : vec_(), size_(0) {

}

template<typename T>
Heap<T>::~Heap() {

}

// O(log n)
template<typename T>
void Heap<T>::Insert(T item) {
  if (size_ == vec_.size())
    vec_.push_back(item);
  else
    vec_[size_] = item;
  bubble_up(size_++);
}

// O(1)
template<typename T>
T Heap<T>::Min() {
  if (size_ == 0)
    return NULL;
  return vec_[0];
}

// O(log n)
template<typename T>
T Heap<T>::ExtractMin() {
  if (size_ == 0)
    return NULL;

  T min   = vec_[0];
  vec_[0] = vec_[--size_];
  heapify(0);

  return min;
}

template<typename T>
void Heap<T>::heapify(int index) {
  if (index >= size_)
    return;

  T lchild_ix = young_child(index);
  T rchild_ix = lchild_ix + 1;
  int min_index = index;

  if (lchild_ix <= size_)
    min_index = (vec_[lchild_ix] < vec_[min_index]) ? lchild_ix : min_index;

  if (rchild_ix <= size_)
    min_index = (vec_[rchild_ix] < vec_[min_index]) ? rchild_ix : min_index;

  if (index != min_index) {
    std::swap(vec_[index], vec_[min_index]);
    heapify(min_index);
  }
}

template<typename T>
void Heap<T>::bubble_up(int index) {
  while (index > 0 && vec_[index] < vec_[parent(index)]) {
    std::swap(vec_[index], vec_[parent(index)]);
    index = parent(index);
  }
}

template<typename T>
int Heap<T>::parent(int index) {
  return (index >> 1);
}

template<typename T>
int Heap<T>::young_child(int index) {
  return (index << 1) + 1;
}

int main() {
  Heap<int> heap;
  heap.Insert(10);
  heap.Insert(17);
  heap.Insert(13);
  heap.Insert(8);
  heap.Insert(19);
  heap.Insert(7);
  std::cout << "Min item: " << heap.Min() << std::endl;

  heap.Insert(4);
  std::cout << "Min item: " << heap.Min() << std::endl;

  heap.Insert(1);
  std::cout << "Min item: " << heap.Min() << std::endl;

  std::cout << std::endl << "The heap: " << std::endl;
  int min;
  while (min = heap.ExtractMin()) {
    std::cout << " -> " << min;
  }

  std::cout << std::endl;
}