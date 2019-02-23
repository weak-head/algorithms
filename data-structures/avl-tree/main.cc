#include "avl-tree.h"
#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

using namespace std;

vector<int> generate_random_array(int num = 1000, int min = 1, int max = 1000) {
  random_device rnd_device;
  mt19937 mersenne_engine { rnd_device() };
  uniform_int_distribution<int> dist {min, max};

  auto gen = [&dist, &mersenne_engine]() {
    return dist(mersenne_engine);
  };

  vector<int> vec(num);
  generate(begin(vec), end(vec), gen);

  return vec;
}

int main(int argc, char **argv) {
  vector<int> a = generate_random_array(100);
  avl::Avl<int> avl;

  for (auto i : a)
    avl.Insert(i);

  avl.Traverse([](int item) { cout << item << ", "; });

  cout << "done" << endl;
  return 0;
}