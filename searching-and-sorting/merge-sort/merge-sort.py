
# the value is used as a hard barrier
# during the merge of two ordered sets.
# By pushing this <max_element> to the bottom
# of stack we can avoid having check for
# the empty stack edge condition
MAX_VALUE = 200

def merge(a, l, m , r):
    '''
    Merge two ordered sub-arrays into ordered array.
    O(n)
    '''
    lq, rq = [MAX_VALUE], [MAX_VALUE]

    for i in range(m-1, l-1, -1):
        lq.append(a[i])

    for i in range (r, m-1, -1):
        rq.append(a[i])

    for i in range(l, r+1):
        a[i] = lq.pop() if (lq[len(lq)-1] < rq[len(rq)-1]) else rq.pop()

def _mergesort(a, l, r):
    if (l >= r):
        return

    pivot = (l + r) >> 1
    _mergesort(a, l, pivot)
    _mergesort(a, pivot + 1, r)
    merge(a, l, pivot + 1, r)

def mergesort(a):
    _mergesort(a, 0, len(a) - 1)

if __name__ == '__main__':
    a = [0, 2, 4, 6, 8, 1, 3, 5, 7]
    mergesort(a)
    print(a)

