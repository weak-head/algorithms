#ifndef AVL_TREE_H_
#define AVL_TREE_H_

namespace avl {

template<typename T>
class AvlNode {
  public:
    AvlNode();
    ~AvlNode();

    const T data() const { return data_; }
    void set_data(const T data) { data_ =  data; }

    const AvlNode<T> parent() const { return parent_; }
    void set_parent(const AvlNode<T> *parent) { parent_ = parent; }

    const AvlNode<T> left() const { return left_; }
    void set_left(const AvlNode<T> *left) { left_ = left; }

    const AvlNode<T> right() const { return right_; }
    void set_right(const AvlNode<T> *right) { right_ = right; }

  private:
    T data_;
    AvlNode<T> *parent_;
    AvlNode<T> *left_;
    AvlNode<T> *right_;
};

template<typename T>
class Avl {
  public:
    Avl();
    ~Avl();

    void Insert(T item);
    void Delete(T item);
    bool Find(T item);

  private:
    AvlNode<T> *root_;
};

} // namespace avl

#endif