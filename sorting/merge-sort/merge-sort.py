import random
import time
from functools import wraps

# the value is used as a hard barrier
# during the merge of two ordered sets.
# By pushing this <max_element> to the bottom
# of stack we can avoid having check for
# the empty stack edge condition
MAX_VALUE = 2000000

PROFILE_DATA = {}

def random_array(size = 100000, min_value = 0, max_value = MAX_VALUE - 1):
    return random.sample(range(min_value, max_value), size)

def profile(fn):
    @wraps(fn)
    def with_profile(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        elapsed_time = time.time() - start_time

        fn_name = fn.__name__
        if fn_name not in PROFILE_DATA:
            PROFILE_DATA[fn_name] = []
        PROFILE_DATA[fn_name].append(elapsed_time)

        total_time = sum(PROFILE_DATA[fn_name])
        avg_time = total_time / len(PROFILE_DATA[fn_name])

        print('{fn_name} finished in {time:.3f} sec, averaging {avg:.3f} sec, total time: {total:.3f} sec'
            .format( fn_name = fn_name
                   , time = elapsed_time
                   , avg = avg_time
                   , total = total_time))
        return res
    return with_profile


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

@profile
def mergesort(a):
    '''
    Idea:
        Recursively divide the collection to simplest case that is already sorted (single element).
        Recursively merge ordered sub-arrays into the final ordered array.

    Complexity:
        O(n * log n)
    '''
    _mergesort(a, 0, len(a) - 1)

if __name__ == '__main__':
    num_elements = 200 * 1000

    for i in range(0, 5):
        a = random_array(size = num_elements)
        mergesort(a)