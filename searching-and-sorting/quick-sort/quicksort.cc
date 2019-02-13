#include <iostream>
#include <vector>

typedef std::vector<int> Array;

int partition(Array& a, int l, int r) {
  int last_min = l, pivot = r;

  for (int i = l; i < r; i++)
    if (a[i] < a[pivot])
      std::swap(a[i], a[last_min++]);

  std::swap(a[last_min], a[pivot]);

  return last_min;
}

void quicksort(Array& a, int l, int r) {
  if (r <= l)
    return;

  int p = partition(a, l, r);
  quicksort(a, l, p - 1);
  quicksort(a, p + 1, r);
}

/*

*/
void quicksort(Array& a) {
  quicksort(a, 0, a.size() - 1);
}

int main() {
  Array a { 12, 1, 2, 7, 13, 20, 9, 0, 42, 17, 5, 8, 4 };

  quicksort(a);

  for (auto i : a)
    std::cout << i << " ";

  std::cout << std::endl;
}