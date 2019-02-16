import random
import time
from functools import wraps

def random_array(num_elements = 100000, el_min_value = 0, el_max_value = 2000000):
    return random.sample(range(el_min_value, el_max_value), num_elements)

PROFILE_DATA = {}
def profile(fn):
    '''
        Profiles how long it takes to run a function,
        accumulating global average
     '''
    @wraps(fn)
    def with_profile(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        elapsed_time = time.time() - start_time

        fn_name = fn.__name__
        if fn_name not in PROFILE_DATA:
            PROFILE_DATA[fn_name] = []
        PROFILE_DATA[fn_name].append(elapsed_time)

        average = sum(PROFILE_DATA[fn_name]) / len(PROFILE_DATA[fn_name])

        print('{fn_name} finished in {time:.3f} sec, averaging {avg:.3f} sec'
            .format( fn_name = fn_name
                   , time = elapsed_time
                   , avg = average))
        return res
    return with_profile

@profile
def quick_sort(a):
    '''
        Quick sort is one of the canonical examples of randomized algorithms.
        In the worst-case (previously sorted array) will run in O(n^2).
        The expected running time is O(n * log n).

        To avoid worst case scenario, some random shuffle could be applied
        th the input collection. As one of the examples is Fisher-Yates, that
        runs in O(n) and dosn't increase the complexity of quick sort, but
        with pretty high probability eliminates the worst case scenario.
     '''
    _quick_sort(a, 0, len(a) - 1)

def _quick_sort(a, l, r):
    if (l >= r):
        return

    pivot = partition(a, l, r)
    _quick_sort(a, l, pivot - 1)
    _quick_sort(a, pivot + 1, r)

def partition(a, l, r):
    '''
        Partition collection in such way that all elements
        that are less or equal than the last one are from the
        left side of it.

        Input:
            [0, 7, 11, 23, 4, 2, 1, 5, 19, 7]

        Output:
            [0, 7, 4, 2, 1, 5, 7, 23, 19, 11]

        Returns:
            The new index of the pivot element
     '''

    last_min, pivot = l, a[r]
    for i in range(l, r):
        if (a[i] <= pivot):
           a[i], a[last_min] = a[last_min], a[i]
           last_min += 1

    a[last_min], a[r] = a[r], a[last_min]

    return last_min


if __name__ == '__main__':
    num_elements = 200 * 1000

    for i in range(0, 5):
        arr = random_array(num_elements = num_elements)
        quick_sort(arr)

    print('-- worst case setup --')
    num_elements = 700
    arr = random_array(num_elements = num_elements)
    quick_sort(arr)
    quick_sort(arr)