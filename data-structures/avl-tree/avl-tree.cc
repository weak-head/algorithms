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

  //       balance < -1 -> Left subtree is higher
  // -1 <= balance <= 1 -> balanced
  //       balance >  1 -> right subree is higher
  int balance = r_height - l_height;

  // left subtree is higher (LL or LR rotation is required)
  if (balance < -1) {
    int ll_height = node->left()->left() ?
                    node->left()->left()->height() : 0;
    int lr_height = node->left()->right() ?
                    node->left()->right()->height() : 0;
    // LL case
    if (ll_height > lr_height)
      return RotateRight(node);
    // LR case
    else {
      node->set_left(RotateLeft(node->left()));
      return RotateRight(node);
    }
  }
  // right subtree is higher (RR or RL rotation is required)
  else if (balance > 1) {
    int rr_height = node->right()->right() ?
                    node->right()->right()->height() : 0;
    int rl_height = node->right()->left() ?
                    node->right()->left()->height() : 0;
    // RR case
    if (rr_height > rl_height)
      return RotateLeft(node);
    // RL case
    else {
      node->set_right(RotateRight(node->right()));
      return RotateLeft(node);
    }
  }
  // the node is in balance
  else {
    int node_height = std::max(l_height, r_height) + 1;
    node->set_height(node_height);
    return node;
  }
}

template<typename T>
AvlNode<T> *Avl<T>::RotateLeft(AvlNode<T> *node) const {
  return node;
}

template<typename T>
AvlNode<T> *Avl<T>::RotateRight(AvlNode<T> *node) const {
  AvlNode<T> *x  = node->left();
  AvlNode<T> *c3 = x->right();

  // rotate the subtree
  x->set_right(node);
  node->set_left(c3);

  // adjust node height
  int node_height = std::max(LeftHeight(node), RightHeight(node)) + 1;
  node->set_height(node_height);

  // adjust x height
  int x_height = std::max(LeftHeight(x), RightHeight(x)) + 1;
  x->set_height(x_height);

  return x;
}

template<typename T>
inline const int Avl<T>::LeftHeight(const AvlNode<T> *node) const {
  return node->left() ? node->left()->height() : 0;
}

template<typename T>
inline const int Avl<T>::RightHeight(const AvlNode<T> *node) const {
  return node->right() ? node->right()->height() : 0;
}

// Defined AVL instances
template class AvlNode<int>;
template class Avl<int>;

} // namespace avl