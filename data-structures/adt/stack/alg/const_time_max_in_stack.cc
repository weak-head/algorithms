#include <iostream>
#include <stack>
#include <array>

using namespace std;

/*
  Maximum in a stack in O(1) time and O(1) extra space.
*/
class MaxStack {
  private:
    stack<int> stack_;
    int max_;

  public:
    /*
      Every time we push element, we need to check if it is new maximum.
      If yes, we are storing composite number that helps us to restore the
      previous maximum when the current maximum is popped out.
    */
    void push(int value) {
      if (stack_.empty()) {
        max_ = value;
        stack_.push(value);
      }
      else if (value > max_) {
        int composite = (value << 1) - max_;
        stack_.push(composite);
        max_ = value;
      }
      else
        stack_.push(value);
    }

    /*
      Every time we pop element, we need to check if it is a current maximum,
      by checking if the composite number if bigger than the maximum.
      If yes, we are restoring the previous maximum.
    */
    int pop() {
      if (empty())
        throw "Stack is empty";

      int value = stack_.top();
      stack_.pop();
      if (value > max_) {
        int old_max = max_;
        max_ = (max_ << 1) - value;
        return old_max;
      }
      else
        return value;
    }

    bool empty() {
      return stack_.empty();
    }

    int max() {
      if (!empty())
        return max_;
      else
        throw "Stack is empty";
    }
};


int main() {
  array<int, 9> a {1, 3, 2, 0, 5, 4, 7, 9, 8};
  MaxStack ms;

  // Output the elements to be inserted into stack
  cout << "=> [";
  for (int i = 0; i < a.size(); i++) {
    cout << a[i];

    if (i != a.size() - 1)
      cout << ", ";
  }
  cout << "]" << endl << endl;

  // Push all elements to stack
  for (int i : a) {
    ms.push(i);
    cout << "push: " << i << "; max: " << ms.max() << endl;
  }
  cout << endl;

  // Pop and output all elements from the stack
  while (!ms.empty()) {
    int max = ms.max();
    int value = ms.pop();

    cout << "pop: " << value << "; max: " << max;

    if (!ms.empty())
      cout << "; new max: " << ms.max() << endl;
    else
      cout << endl;
  }

  cout << endl;
  return 0;
}