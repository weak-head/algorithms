#include <iostream>
#include <vector>

typedef std::vector<int> Array;

// O(n * log n)
void merge_sort(Array& a) {
  merge_sort(a, 0, a.size() - 1);
}

void merge_sort(Array& a, int left, int right) {
  if (left >= right)
    return;

  int mid = (left + right) >> 1;
  merge_sort(a, left, mid);
  merge_sort(a, mid + 1, right);
  merge(a, left, mid, right);
}

void merge(Array& a, int left, int mid, int right) {

}

void main() {

}