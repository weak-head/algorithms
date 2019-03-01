# algorithms

## Combinatorial

- permutations
  - [fisher-yates shuffle](combinatorial/permutations/fisher-yates-shuffle.hs)

## Number theory

- primes
  - [sieve eratosthenes](number-theory/primes/sieve-eratosthenes/primes-sieve-eratosthenes.hs)

## Searching and sorting

- sorting
  - [bubble](searching-and-sorting/bubble-sort/bubble-sort.hs)
  - [selection](searching-and-sorting/selection-sort/selection.cc)
  - [insertion](searching-and-sorting/insertion-sort/insertion-sort.hs)
  - [heapsort](searching-and-sorting/heap-sort/heapsort.cc)
  - [mergesort](searching-and-sorting/merge-sort/merge-sort.cc)
  - [quicksort](searching-and-sorting/quick-sort/quicksort.cc)
  - todo: shellsort
  - todo: bucket sort

## NP hard

- tsp
  - [nearest neighbor](np-hard/tsp/nearest-neighbor.py)
  - [closest pair](np-hard/tsp/closest-pair.py)

## Data structures

- abstract data types
  - queue
    - [double ended](data-structures/adt/queue/double-ended-queue.py)
    - [linked list](data-structures/adt/queue/queue-linked-list.py)
  - stack
    - [linked list](data-structures/adt/stack/stack-linked-list.py)
    - [[alg] balanced parentheses](data-structures/adt/stack/alg/parentheses-match.py)
    - [[alg] max elem in O(1)](data-structures/adt/stack/alg/const_time_max_in_stack.cc)
  - priority queue
    - [linked list](data-structures/adt/priority-queue/priority-queue-linked-list.hs)
    - [sorted dynamic array](data-structures/adt/priority-queue/priority-queue-sorted-array.cpp)
    - [heap](data-structures/heap/heap.cc)
- array
  - [dynamic array](data-structures/array/dynamic-array.cpp)
  - [parallel array](data-structures/array/parallel-array.py)
  - [circular buffer](data-structures/array/circular-buffer.cpp)
  - [[alg] matrix multiplication](data-structures/array/alg/matrix-multiplication.py)
  - [[alg] transpose](data-structures/array/alg/transpose.hs)
- list
  - [singly linked list](data-structures/list/singly-linked-list.py)
  - [doubly linked list](data-structures/list/doubly-linked-list.py)
  - [self-organizing list](data-structures/list/self-organizing-list.py)
  - [skip list](data-structures/list/skip-list.py)
  - [unrolled linked list](data-structures/list/unrolled-linked-list.py)
  - [difference list](data-structures/list/difference-list.hs)
  - [[alg] reverse linked list](data-structures/list/alg/reverse-linked-list.py)
  - [[alg] find middle node](data-structures/list/alg/mid-node.py)
  - [[alg] detect loop](data-structures/list/alg/loop-in-linked-list.py)
- hash table
  - [separate chaining](data-structures/hash-table/separate-chaining-hash-table.py)
  - [open addressing](data-structures/hash-table/open-addressing-hash-table.py)
- heap
  - [heap](data-structures/heap/heap.cc)
  - [[alg] k-th greater than x](data-structures/heap/kth-greater-x-heap.cc)
- search tree
  - [unbalanced binary tree](data-structures/binary-tree/binary-tree.py)
  - [avl tree](data-structures/avl-tree/avl-tree.cc)
  - todo: b tree
  - todo: b+ tree
  - todo: red-black tree
  - todo: 2-3 tree
  - todo: trie
  - [[alg] n-th min in BST](data-structures/binary-tree/alg/nth-min.py)
  - [[alg] merge two BST](data-structures/binary-tree/alg/merge-two-bst.py)
  - [[alg] O(1) suc/pred in BST](data-structures/binary-tree/alg/bst-suc-pred.py)
  - [[alg] compare two BST](data-structures/binary-tree/alg/compare-two-bst.py)
- other
  - [lru cache](data-structures/other/lru-cache/lru-cache.py)