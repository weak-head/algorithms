#include "avl-tree.h"
#include <iostream>

using namespace std;

int main(int argc, char **argv) {
  avl::Avl<int> avl;
  avl.Insert(10);
  avl.Insert(15);
  avl.Insert(18);
  cout << "done" << endl;
}