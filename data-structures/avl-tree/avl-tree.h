#ifndef AVL_TREE_H_
#define AVL_TREE_H_

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

    const AvlNode<T> parent() const { return parent_; }
    void set_parent(const AvlNode<T> *parent) { parent_ = parent; }

    const AvlNode<T> left() const { return left_; }
    void set_left(const AvlNode<T> *left) { left_ = left; }

    const AvlNode<T> right() const { return right_; }
    void set_right(const AvlNode<T> *right) { right_ = right; }

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
    AvlNode<T> *Find(const T item) const;

  private:
    AvlNode<T> *root_;
};

} // namespace avl

#endif