import random
import time
from functools import wraps

def random_array(el_num = 100000, min_val = 0, max_val = 2000000):
    return random.sample(range(min_val, max_val), el_num)

PROFILE_DATA = {}
def profile(fn):
    @wraps(fn)
    def func_wrap(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        elapsed_time = time.time() - start_time

        fn_name = fn.__name__
        if fn_name not in PROFILE_DATA:
            PROFILE_DATA[fn_name] = []
        PROFILE_DATA[fn_name].append(elapsed_time)

        total = sum(PROFILE_DATA[fn_name])
        avg = total / len(PROFILE_DATA[fn_name])

        print('{fn_name} has finished in {time:.3f} sec, averaging {avg:.3f} sec, total time {total:.3f} sec'
            .format( fn_name = fn_name
                   , time = elapsed_time
                   , avg = avg
                   , total = total))

        return res
    return func_wrap

def heapify(a, ix):
    '''
        The key operation in the heapsort.
        Tries to move the specified element down the priority queue.

        O(log n)
    '''
    if ix >= len(a):
        return

    l_child = ix << 1
    r_child = l_child + 1
    min_el  = ix

    if l_child < len(a):
        min_el = l_child if a[l_child] < a[min_el] else min_el

    if r_child < len(a):
        min_el = r_child if a[r_child] < a[min_el] else min_el

    if min_el != ix:
        a[min_el], a[ix] = a[ix], a[min_el]
        heapify(a, min_el)

def reorganize_to_pqueue(a):
    '''
        Reorganize a collection to shape it into a priority queue.
        O (log n)
    '''
    for i in range(len(a) >> 1, -1, -1):
        heapify(a, i)

def extract_min(a):
    '''
    Extract the top element from priority queue making sure that
    priority queue invariants are not broken.
    '''
    if len(a) <= 0:
        return None

    min, a[0] = a[0], a[len(a) - 1]
    a.pop()

    heapify(a, 0)

    return min

@profile
def heapsort(a):
    '''
        The heapsort could be seen as greatly improved version
        of the selection sort that takes adventage of the priority queue.

        It takes O(log n) to build a priority queue and O(log n)
        to extract a top element from the queue.

        The total running time is O(n * log n).

        One downside of heapsort is that it requires O(n) additional space
        for the priority queue.
    '''
    pq = list(a)
    reorganize_to_pqueue(pq)

    for i in range(0, len(a)):
        a[i] = extract_min(pq)

if __name__ == '__main__':
    el_num = 200 * 1000
    for i in range(0, 5):
        a = random_array(el_num)
        heapsort(a)