#include <iostream>
#include <vector>

#include <random>
#include <algorithm>
#include <iterator>
#include <functional>

using namespace std;

typedef std::vector<int> Array;

int partition(Array& a, int l, int r) {
  int last_min = l, pivot = r;

  for (int i = l; i < r; i++)
    if (a[i] < a[pivot])
      swap(a[i], a[last_min++]);

  swap(a[last_min], a[pivot]);

  return last_min;
}

void quicksort(Array& a, int l, int r) {
  if (r <= l)
    return;

  int p = partition(a, l, r);
  quicksort(a, l, p - 1);
  quicksort(a, p + 1, r);
}

// O(n)
void fisher_yates_shuffle(Array& a) {
  random_device rnd_device;
  mt19937 mersenne_engine(rnd_device());

  for (int i = a.size() - 1; i > 0; i--) {
    uniform_int_distribution<int> dist(0, i - 1);
    int j = dist(mersenne_engine);

    swap(a[i], a[j]);
  }
}

/*
  By relying on random shuffle we can avoid
  the worst case running time O(n^2) with pretty
  high probability.

  Without the shuffle, previously sorted array
  will result in the worst case running time.
*/
void quicksort(Array& a) {
  fisher_yates_shuffle(a);
  quicksort(a, 0, a.size() - 1);
}

Array generate_random_array() {
  random_device rnd_device;
  mt19937 mersenne_engine { rnd_device() };
  uniform_int_distribution<int> dist {1, 100};

  auto gen =
    [&dist, &mersenne_engine]() {
      return dist(mersenne_engine);
    };

  vector<int> vec(30);
  generate(begin(vec), end(vec), gen);

  return vec;
}

int main() {
  Array a = generate_random_array();

  quicksort(a);

  for (auto i : a)
    cout << i << " ";

  cout << endl;
}