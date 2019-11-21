import time
import random
from functools import wraps

# --------------------------------------------------------------------

PROF_DATA = {}


def profile(fn):
    @wraps(fn)
    def with_profile(*args, **kwargs):
        start_time = time.time()

        ret = fn(*args, **kwargs)

        elapsed_time = time.time() - start_time

        name = fn.__name__
        if name not in PROF_DATA:
            PROF_DATA[name] = [0, []]
        PROF_DATA[name][0] += 1
        PROF_DATA[name][1].append(elapsed_time)

        return ret

    return with_profile


def print_prof_data():
    for name, data in PROF_DATA.items():
        max_time = max(data[1])
        avg_time = sum(data[1]) / len(data[1])
        print("%s called %d times." % (name, data[0]))
        print("Time [max]: %.3f, [average]: %.3f" % (max_time, avg_time))


# --------------------------------------------------------------------

@profile
def insertion_sort(lst):
    for j in range(len(lst)):
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1], j = lst[j-1], lst[j], j-1


# --------------------------------------------------------------------

def run():
    n = 10000
    for i in range(0, 10):
        lst = random.sample(range(1, n+1000), n)
        insertion_sort(lst)
    print_prof_data()
