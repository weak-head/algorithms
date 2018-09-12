#include <iostream>
#include <vector>

using namespace std;

// Priority queue that is based on sorted array
//
// Insert: O(n)
// Peek: O(1)
// Delete: O(1)
//
template <typename T>
class PriorityQueue {
private:
  vector<T> queue;

public:
  void insert(T item);
  T peek();
  void deleteMin();

  void print();
};

// O(n)
template<typename T>
void PriorityQueue<T>::insert(T item) {
  // O(log n)
  int l = 0;
  int r = this->queue.size();
  while (l < r) {
    int i = l + ((r - l) / 2);
    if (this->queue[i] >= item) { l = i + 1; } else { r = i - 1; }
  }

  vector<int>::iterator it = this->queue.begin() + l;
  // O(n)
  this->queue.insert(it, item);
}

// O(1)
template<typename T>
T PriorityQueue<T>::peek() {
  return this->queue.back();
}

// O(1)
template<typename T>
void PriorityQueue<T>::deleteMin() {
  this->queue.pop_back();
}

// O(n)
template<typename T>
void PriorityQueue<T>::print() {
  for (vector<int>::iterator it = this->queue.begin(); it != this->queue.end(); ++it) {
    cout << ' ' << *it;
  }
  cout << '\n';
}

int main() {
  PriorityQueue<int> queue;

  cout << "+5" << '\n';
  queue.insert(5);
  queue.print();

  cout << "+2" << '\n';
  queue.insert(2);
  queue.print();

  cout << "+8" << '\n';
  queue.insert(8);
  queue.print();

  cout << "+10" << '\n';
  queue.insert(10);
  queue.print();

  cout << "+3" << '\n';
  queue.insert(3);
  queue.print();

  cout << "+0" << '\n';
  queue.insert(0);
  queue.print();

  cout << "peek: " << queue.peek() << '\n';
  queue.deleteMin();
  cout << "peek: " << queue.peek() << '\n';
  queue.deleteMin();
  cout << "peek: " << queue.peek() << '\n';
}