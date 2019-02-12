#include <iostream>

#include <limits>
#include <vector>
#include <queue>

typedef std::vector<int> Array;
typedef std::queue<int> Queue;

void merge(Array& a, int left, int mid, int right) {
  Queue ql, qr;
  int infinity = std::numeric_limits<int>::max();

  for (int i = left; i < mid; i++)
    ql.push(a[i]);
  ql.push(infinity);

  for (int i = mid; i <= right; i++)
    qr.push(a[i]);
  qr.push(infinity);

  for (int i = left; i <= right; i++)
    if (ql.front() < qr.front()) {
      a[i] = ql.front();
      ql.pop();
    } else {
      a[i] = qr.front();
      qr.pop();
    }
}

void merge_sort(Array& a, int left, int right) {
  if (left >= right)
    return;

  int mid = (left + right) >> 1;
  merge_sort(a, left, mid);
  merge_sort(a, mid + 1, right);
  merge(a, left, mid + 1, right);
}

// O(n * log n)
void merge_sort(Array& a) {
  merge_sort(a, 0, a.size() - 1);
}

int main() {
  Array a {2, 4, 9, 1, 12, 3, 6, 7, 5, 23, 0};
  merge_sort(a);

  for (auto i : a)
    std::cout << i << " ";

  std::cout << std::endl;
}