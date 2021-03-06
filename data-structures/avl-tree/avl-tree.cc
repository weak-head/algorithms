#include "avl-tree.h"
#include <algorithm>
#include <functional>
#include <queue>

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
bool Avl<T>::Find(const T item) const {
  return Find(root_, item);
}

template<typename T>
void Avl<T>::Delete(const T data) {
  root_ = Delete(root_, data);
}

template<typename T>
void Avl<T>::Traverse(std::function<void(T)> callback,
                      const Traversal traversal) const {
  if (traversal == Traversal::Levelorder)
    BreadthFirstTraverse(root_, callback);
  else
    DepthFirstTraverse(root_, callback, traversal);
}

template<typename T>
AvlNode<T>* Avl<T>::Insert(AvlNode<T> *node, const T data) {
  if (!node)
    return new AvlNode<T>(data);

  // recursively insert the data
  // into the appropriate subtree
  if (node->data() < data) {
    AvlNode<T> *r_node = Insert(node->right(), data);
    node->set_right(r_node);
    r_node->set_parent(node);
  }
  else {
    AvlNode<T> *l_node = Insert(node->left(), data);
    node->set_left(l_node);
    l_node->set_parent(node);
  }

  return Rebalance(node);
}

template<typename T>
AvlNode<T> *Avl<T>::Delete(AvlNode<T> *node, const T data) {
  if (!node)
    return NULL;

  // recursively delete node from the
  // appropriate subtree.
  // Search for the node in the right subtree
  if (node->data() < data) {
    AvlNode<T> *r_node = Delete(node->right(), data);
    node->set_right(r_node);
    if (r_node)
      r_node->set_parent(node);
  }
  // Search for the node in the left subtree
  else if (node->data() > data) {
    AvlNode<T> *l_node = Delete(node->left(), data);
    node->set_left(l_node);
    if (l_node)
      l_node->set_parent(node);
  }
  // The node that we want to delete
  else {
    // Single child or no children at all
    if (!node->left() || !node->right()) {
      AvlNode<T> *child = node->left() ? node->left() : node->right();

      // No child
      if (!child)
      {
        delete node;
        return NULL;
      }

      AvlNode<T> *node_to_delete = node;
      node = child;

      // Delete the node without it's children
      node_to_delete->set_left(NULL);
      node_to_delete->set_right(NULL);
      delete node_to_delete;
    }
    // Two children
    else {
      AvlNode<T> *left_most = MaxNode(node->left());

      // Replace the data
      node->set_data(left_most->data());

      // Delete the left most
      AvlNode<T> *l_node = Delete(node->left(), node->data());
      node->set_left(l_node);
      if (l_node)
        l_node->set_parent(node);
    }
  }

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

  // adjust parent-child relations
  x->set_parent(node->parent());
  node->set_parent(x);
  if (c3)
    c3->set_parent(node);

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

  // adjust parent-child relations
  x->set_parent(node->parent());
  node->set_parent(x);
  if (c3)
    c3->set_parent(node);

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

template<typename T>
const AvlNode<T> *Avl<T>::Find(const AvlNode<T> *node, T item) const {
  if (!node)
    return 0;

  if (node->data() == item)
    return node;

  if (node->data() < item)
    return Find(node->right(), item);
  else
    return Find(node->left(), item);
}

template<typename T>
AvlNode<T> *Avl<T>::MaxNode(AvlNode<T> *node) const {
  AvlNode<T> *max_node = node;

  while(max_node->right())
    max_node = max_node->right();

  return max_node;
}

template<typename T>
void Avl<T>::DepthFirstTraverse(const AvlNode<T> *node,
                                std::function<void(T)> callback,
                                const Traversal traversal) const {
  if (!node)
    return;

  if (traversal == Traversal::Preorder)
    callback(node->data());

  DepthFirstTraverse(node->left(), callback, traversal);

  if (traversal == Traversal::Inorder)
    callback(node->data());

  DepthFirstTraverse(node->right(), callback, traversal);

  if (traversal == Traversal::Postorder)
    callback(node->data());
}

template<typename T>
void Avl<T>::BreadthFirstTraverse(const AvlNode<T> *node,
                                  std::function<void(T)> callback) const {
  if (!node)
    return;

  std::queue<const AvlNode<T>*> order;
  order.push(node);

  while (!order.empty()) {
    auto next = order.front();

    callback(next->data());
    order.pop();

    if (next->left())
      order.push(next->left());

    if (next->right())
      order.push(next->right());
  }
}

// Defined AVL instances
template class AvlNode<int>;
template class Avl<int>;

} // namespace avl