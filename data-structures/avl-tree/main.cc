#include "avl-tree.h"
#include <iostream>
#include <iomanip>
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

void print_avl(avl::Avl<int> *tree) {
  cout << "Inorder: [";
  tree->Traverse([](int item) {
        cout << setfill('0') << setw(3) << item;
        cout << ", ";
      });
  cout << "]";
  cout << endl;

  cout << "Level:   [";
  tree->Traverse([](int item) {
        cout << setfill('0') << setw(3) << item;
        cout << ", ";
      }, avl::Traversal::Levelorder);
  cout << "]";
}

int main(int argc, char **argv) {
  vector<int> a = generate_random_array(20);
  avl::Avl<int> avl;

  for (auto i : a) {
    cout << "ins: " << i << endl;

    avl.Insert(i);
    print_avl(&avl);

    cout << endl << endl;
  }

  for (auto i : a) {
    cout << "del: " << i << endl;

    avl.Delete(i);
    print_avl(&avl);

    cout << endl << endl;
  }

  cout << "<done>" << endl;
  return 0;
}