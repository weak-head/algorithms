#include "avl-tree.h"
#include <algorithm>

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

  // recursively insert the data
  // into the correct subtree
  if (node->data() < data)
    node->set_left(Insert(node->right(), data));
  else
    node->set_right(Insert(node->left(), data));

  return Rebalance(node);
}

template<typename T>
AvlNode<T>* Avl<T>::Rebalance(AvlNode<T> *node) const {
  int l_height = node->left()  ? node->left()->height()  : 0;
  int r_height = node->right() ? node->right()->height() : 0;

  int node_height = std::max(l_height, r_height) + 1;
  //       balance < -1 -> Left subtree is higher
  // -1 <= balance <= 1 -> balanced
  //       balance >  1 -> right subree is higher
  int balance = r_height - l_height;

  //node->set_height(node_height);
  return node;
}


// Defined AVL instances
template class AvlNode<int>;
template class Avl<int>;

} // namespace avl