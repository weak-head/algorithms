#include <iostream>

/*
  Circular buffer that is based on the array.

  This implementation is not thread-safe, and doesn't cover any multi-threaded scenarios.
  Retrieving object from the buffer returns address of the object in the array.
  This could result into situation when the retrieved data is being overwritten by the consequent 'put'.

*/
template <typename T>
class CircularBuffer {
private:
  int size;
  int start;
  int end;
  bool full;
  T *head;

public:
  CircularBuffer(int size) {
    this->size = size;
    this->head = new T[size];
    this->start = 0;
    this->end = 0;
    this->full = false;
  }

  void put(T item) {
    // overwriting first item
    if ((this->start == this->end) && (this->full)) {
      this->start = (this->start + 1) % this->size;
    }

    this->head[this->end] = item;
    this->end = (this->end + 1) % this->size;

    // buffer is full, the next put will overwrite
    if (this->end == this->start) {
      this->full = true;
    }
  }

  T* get() {
    if (this->start == this->end && !this->full) {
      return NULL;
    }

    T* v = &this->head[this->start]; // optionally memcpy to a new location
    this->start = (this->start + 1) % this->size;
    this->full = false;

    return v;
  }

  void show() {
    // empty buffer
    if (this->start == this->end && !this->full) {
      return;
    }

    bool step = false;
    for (int i = this->start; (i != this->end) || !step; i = (i+1) % this->size) {
      std::cout << this->head[i];
      if ((i + 1) % this->size != this->end) { std::cout << " <- "; }
      step = true;
    }
    std::cout << std::endl;
  }
};


int main()
{
  CircularBuffer<int> cbuf(5);

  for (int i = 1; i <= 15; i++)
  {
    std::cout << "put " << i << ": ";
    cbuf.put(i);
    cbuf.show();
  }

  std::cout << std::endl;

  for (int *value = cbuf.get(); value != NULL; value = cbuf.get())
  {
    std::cout << "get > " << *value << "; buf: ";
    cbuf.show();
  }

  return 0;
}