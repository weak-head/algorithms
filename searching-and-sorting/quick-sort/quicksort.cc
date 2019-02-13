#include <iostream>
#include <vector>

typedef std::vector<int> Array;

/*

*/
void quicksort(Array& a) {
  quicksort(a, 0, a.size() - 1);
}

void quicksort(Array& a, int l, int r) {
  if (r < l)
    return;

  int p = partition(a, l, r);
  quicksort(a, l, p - 1);
  quicksort(a, p + 1, r);
}

int partition(Array& a, int l, int r) {

}

int main() {

}