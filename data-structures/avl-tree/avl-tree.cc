#include "avl-tree.h"

namespace avl {

// Any leaf node in the AVL tree has a height of one.
template<typename T>
AvlNode<T>::AvlNode(const T data)
  : data_(data), left_(0), right_(0), parent_(0), height_(1) {
}

template<typename T>
AvlNode<T>::~AvlNode() {
  if (left_)
    delete left_;
  if (right_)
    delete right_;
}

template<typename T>
Avl<T>::Avl()
  : root_(0) {
};

template<typename T>
Avl<T>::~Avl() {
  delete root_;
}

// Defined AVL instances
template class Avl<int>;

} // namespace avl