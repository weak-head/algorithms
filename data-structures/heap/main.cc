#include "heap.h"
#include "kth-greater-x-heap.h"

#include <iostream>

using namespace std;

int main(int argc, char **argv) {
  heap::Heap<int> heap;
  heap.Insert(10);
  heap.Insert(17);
  heap.Insert(13);
  heap.Insert(8);
  heap.Insert(19);
  heap.Insert(7);
  cout << "Min item: " << heap.Min() << endl;

  heap.Insert(4);
  cout << "Min item: " << heap.Min() << endl;

  heap.Insert(1);
  cout << "Min item: " << heap.Min() << endl;

  cout << endl << "The heap: " << endl;
  int min;
  while (min = heap.ExtractMin()) {
    cout << " -> " << min;
  }

  cout << endl;
}