#include <iostream>

/*
  Very simplified, list-like dynamic array.
*/
template <typename T>
class DynamicArray {
private:
  const float GROWTH_FACTOR = 1.4;
  int max_capacity;
  int current_size;
  T *head;

public:
  DynamicArray();
  ~DynamicArray();

  T& operator[] (int);

  void append(T);
  void remove(T);

  void print();
};

template <typename T>
DynamicArray<T>::DynamicArray() {
  this->max_capacity = 10;
  this->current_size = 0;
  this->head = new T[this->max_capacity];
}

template <typename T>
DynamicArray<T>::~DynamicArray() {
  if (this->head) {
    delete[] this->head;
    this->head = NULL;
  }
}

template <typename T>
T& DynamicArray<T>::operator[] (int ix) {
  if (ix >= this->current_size) {
    std::cout << "Array index out of bound";
    exit(0);
  }
  return head[ix];
}

template <typename T>
void DynamicArray<T>::append(T data) {
  // the array is full, we need to allocate a new bigger one
  if (this->current_size == this->max_capacity) {
    int new_capacity = static_cast<int>(this->max_capacity * GROWTH_FACTOR);
    T* new_head = new T[new_capacity];

    for (int ix = 0; ix < this->current_size; ix++)
      new_head[ix] = this->head[ix];

    delete[] this->head;
    this->head = new_head;
    this->max_capacity = new_capacity;
  }

  this->head[this->current_size] = data;
  this->current_size++;
}

template<typename T>
void DynamicArray<T>::remove(T data) {
  for (int i = 0; i < this->current_size; i++) {
    if (this->head[i] == data) {
      for (int j = i; j < this->current_size - 1; j++)
        this->head[j] = this->head[j+1];
      this->current_size--;
    }
  }
}

template<typename T>
void DynamicArray<T>::print() {
  std::cout << "max_size: " << this->max_capacity << std::endl;
  std::cout << "cur_size: " << this->current_size << std::endl;

  std::cout << "[";
  for (int i = 0; i < this->current_size; i++) {
    std::cout << this->head[i];
    if (i != this->current_size - 1) {
      std::cout << ",";
    }
  }
  std::cout << "]" << std::endl;
}


int main() {
  DynamicArray<int> dyn_arr;

  for (int i = 1; i < 19; i++) {
    dyn_arr.append(i);
  }
  dyn_arr.print();

  std::cout << std::endl;
  dyn_arr.remove(1);
  dyn_arr.remove(5);
  dyn_arr.remove(10);
  dyn_arr.remove(18);
  dyn_arr.print();

  std::cout << std::endl;
  std::cout << "ix 1: " << dyn_arr[1] << std::endl;
  dyn_arr[1] = 19;
  std::cout << "ix 1: " << dyn_arr[1] << std::endl;
  dyn_arr.print();
}