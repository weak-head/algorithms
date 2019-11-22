# Select N-th min element in linear time
# Randomized select similar to quicksort

import random

def ith(a, nth):
    """ O(n) expected time """
    l, r = 0, len(a) - 1
    if nth < l or nth > r:
        return None

    p = partition(a, l, r)
    while p != nth:
        if p < nth:
            l = p + 1
            p = partition(a, l, r)
        else:
            r = p - 1
            p = partition(a, l, r)
    return a[p]

def partition(a, l, r):
    # ensure we have randomized partitioning
    # to avoid worst case scenario of O(n^2)
    n = random.randint(l, r)
    a[r], a[n] = a[n], a[r]

    # same partitioning logic as in the quicksort
    lix = l-1
    for i in range(l, r):
        if a[i] <= a[r]:
            lix += 1
            a[lix], a[i] = a[i], a[lix]

    lix += 1
    a[lix], a[r] = a[r], a[lix]
    return lix


if __name__ == "__main__":
    a = [90,60,70,80,0,20,30,10,40,50]
    for i in range(10):
        print("({0}) => {1}".format(i, ith(a, i)))

    print("\nverification using sorted array:")
    a, n = [], 30
    for i in range(n):
        a.append(random.randint(0, 2000))

    b = sorted(a)
    for i in range(n):
        av, bv = ith(a, i), b[i]
        if av == bv:
            print("{0:04d} == {1:04d}".format(av, bv))
        else:
            print(" -- error -- ")
            print("{0:04d} != {1:04d}".format(av, bv))
            print(" -- error -- ")