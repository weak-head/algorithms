#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> Array;

/*
  The idea:
    Pick the smallest element from the unsorted set
    and put it as the last element of the sorted set.

  Selection sort + Priority queue = Heapsort
*/
void selection_sort(Array& a) {
  for (int i = 0; i < a.size(); i++) {

    int min = i;
    for (int j = i + 1; j < a.size(); j++)
      if (a[min] > a[j])
        min = j;

    swap(a[i], a[min]);
  }
};

int main() {
  Array a { 17, 23, 1, 3, 7, 11, 18, 4, 0, 5, 9 };
  selection_sort(a);

  for (auto i : a)
    cout << i << " ";

  cout << endl;
}