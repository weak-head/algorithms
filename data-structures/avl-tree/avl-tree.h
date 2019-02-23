#ifndef AVL_TREE_H_
#define AVL_TREE_H_

#include <functional>

namespace avl {

/*
    A node in the AVL tree.
*/
template<typename T>
class AvlNode {
  public:
    AvlNode(const T data);
    ~AvlNode();

    const T data() const { return data_; }
    void set_data(const T data) { data_ =  data; }

    AvlNode<T> *parent() const { return parent_; }
    void set_parent(AvlNode<T> *parent) { parent_ = parent; }

    AvlNode<T> *left() const { return left_; }
    void set_left(AvlNode<T> *left) { left_ = left; }

    AvlNode<T> *right() const { return right_; }
    void set_right(AvlNode<T> *right) { right_ = right; }

    const int height() const { return height_; }
    int set_height(const int height) { height_ = height; }

  private:
    T data_;                // The actual data
    AvlNode<T> *parent_;    // Parent node
    AvlNode<T> *left_;      // Left node
    AvlNode<T> *right_;     // Right node
    int height_;            // Height of this node
};

/*
  Possible AVL tree traversals:
    Depth First:
      - Inorder (Left, Root, Right)
      - Preorder (Root, Left, Right)
      - Postorder (Left, Right, Root)

    Breadth First:
      - Levelorder
*/
enum class Traversal {
  Inorder,
  Preorder,
  Postorder,
  Levelorder
};

/*
    Balanced binary tree in which
    the difference between height
    of right and left sub-trees is
    no more than one.

    All operations are O(ln n)
    Required space: O(n)
*/
template<typename T>
class Avl {
  public:
    Avl();
    ~Avl();

    void Insert(const T item);
    bool Delete(const T item);
    bool Find(const T item) const;
    void Traverse(std::function<void(T)> callback,
                  const Traversal traversal = Traversal::Inorder) const;

  protected:
    // Insert the data into the subtree and return a new subtree root.
    AvlNode<T> *Insert(AvlNode<T> *node, const T data);

    // Re-balance the sub-tree considering the height of it's
    // left and right siblings. New root of the subtree is returned.
    AvlNode<T> *Rebalance(AvlNode<T> *node) const;

    AvlNode<T> *RotateLeft(AvlNode<T> *node) const;
    AvlNode<T> *RotateRight(AvlNode<T> *node) const;

    const int NodeHeight(const AvlNode<T> *node) const;
    const int LeftHeight(const AvlNode<T> *node) const;
    const int RightHeight(const AvlNode<T> *node) const;

    void DepthFirstTraverse(const AvlNode<T> *node,
                            std::function<void(T)> callback,
                            const Traversal traversal) const;
    void BreadthFirstTraverse(const AvlNode<T> *node,
                              std::function<void(T)> callback) const;

  private:
    AvlNode<T> *root_;
};

} // namespace avl

#endif