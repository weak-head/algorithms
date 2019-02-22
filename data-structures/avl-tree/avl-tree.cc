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
  // into the appropriate subtree
  if (node->data() < data)
    node->set_left(Insert(node->right(), data));
  else
    node->set_right(Insert(node->left(), data));

  return Rebalance(node);
}

template<typename T>
AvlNode<T>* Avl<T>::Rebalance(AvlNode<T> *node) const {
  int l_height = LeftHeight(node);
  int r_height = RightHeight(node);

  //       balance < -1 -> Left subtree is higher
  // -1 <= balance <= 1 -> balanced
  //       balance >  1 -> right subree is higher
  int balance = r_height - l_height;

  // left subtree is higher (LL or LR rotation is required)
  if (balance < -1) {
    int ll_height = LeftHeight(node->left());
    int lr_height = RightHeight(node->left());

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
    int rr_height = RightHeight(node->right());
    int rl_height = LeftHeight(node->right());

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
    node->set_height(NodeHeight(node));
    return node;
  }
}

template<typename T>
AvlNode<T> *Avl<T>::RotateLeft(AvlNode<T> *node) const {
  AvlNode<T> *x  = node->right();
  AvlNode<T> *c3 = x->left();

  // rotate the subtree
  node->set_right(c3);
  x->set_left(node);

  // adjust the height of the nodes
  node->set_height(NodeHeight(node));
  x->set_height(NodeHeight(x));

  return x;
}

template<typename T>
AvlNode<T> *Avl<T>::RotateRight(AvlNode<T> *node) const {
  AvlNode<T> *x  = node->left();
  AvlNode<T> *c3 = x->right();

  // rotate the subtree
  node->set_left(c3);
  x->set_right(node);

  // adjust the height of the nodes
  node->set_height(NodeHeight(node));
  x->set_height(NodeHeight(x));

  return x;
}

template<typename T>
inline const int Avl<T>::NodeHeight(const AvlNode<T> *node) const {
  return std::max(LeftHeight(node), RightHeight(node)) + 1;
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