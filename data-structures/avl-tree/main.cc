#include "avl-tree.h"
#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

using namespace std;

vector<int> generate_random_array() {
  random_device rnd_device;
  mt19937 mersenne_engine { rnd_device() };
  uniform_int_distribution<int> dist {1, 1000};

  auto gen = [&dist, &mersenne_engine]() {
    return dist(mersenne_engine);
  };

  vector<int> vec(500);
  generate(begin(vec), end(vec), gen);

  return vec;
}

int main(int argc, char **argv) {
  vector<int> a = generate_random_array();
  avl::Avl<int> avl;

  for (auto i : a)
    avl.Insert(i);

  cout << "done" << endl;
  return 0;
}