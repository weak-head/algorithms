from typing import List
import random
import time
from functools import wraps

def random_array(num_elements = 100000, el_min_value = 0, el_max_value = 2000000):
    return random.sample(range(el_min_value, el_max_value), num_elements)

PROFILE_DATA = {}
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

        total_runs  = len(PROFILE_DATA[fn_name])
        total_time  = sum(PROFILE_DATA[fn_name])
        avg_time = total_time / total_runs

        print('{fn_name} finished in {time:.3f} sec, averaging {avg:.3f} sec, total time: {total:.3f} sec'
            .format( fn_name = fn_name
                   , time = elapsed_time
                   , avg = avg_time
                   , total = total_time))
        return res
    return with_profile

@profile
def shell_sort(arr: List) -> List:
    '''
    It's hard to give any exact estimation of the complexity,
    for the Marcin Cluga's gap sequency.
    '''
    length = len(arr)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        for i in range(gap, length):
            temp, j = arr[i], i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp

if __name__ == '__main__':
    num_elements = 200 * 1000

    for i in range(0, 5):
        arr = random_array(num_elements = num_elements)
        shell_sort(arr)