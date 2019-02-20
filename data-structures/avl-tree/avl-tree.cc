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

template<typename T>
void Avl<T>::Insert(const T data) {
  root_ = Insert(root_, data);
}

template<typename T>
AvlNode<T>* Avl<T>::Insert(AvlNode<T> *node, const T data) {
  if (!node)
    return new AvlNode<T>(data);

  if (node->data() < data)
    node->set_left(Insert(node->right(), data));
  else
    node->set_right(Insert(node->left(), data));

  return node;
}

// Defined AVL instances
template class AvlNode<int>;
template class Avl<int>;

} // namespace avl