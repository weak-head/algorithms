# -- Counting sort --
#
# Because the correct implementation of counting sort
# is stable, we can apply it to run radix sort of an elements 
# by multiple fields

import random

def sort(a, max_value, get_value):
    res = [0] * len(a)
    cnt = [0] * max_value 

    for j in range(len(a)):
        cnt[get_value(a[j])] += 1

    for j in range(1, max_value):
        cnt[j] += cnt[j-1]

    # enumerate indexes from len 
    # down to 0 to make it stable
    for j in range(len(a) - 1, -1, -1):
        res[cnt[get_value(a[j])] - 1] = a[j]
        cnt[get_value(a[j])] -= 1

    return res

class Date:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def __repr__(self):
        return "{0} - {1:02d} - {2:02d}".format(self.year, self.month, self.day)

def generate_dates(n, start_year=1980, end_year=2000):
    # this function could generate non-existing dates, 
    # but for this test we don't care, because that's not the point
    for _ in range(n):
        yield Date(
            random.randint(start_year, end_year),
            random.randint(1, 12),
            random.randint(1, 30)
        )

if __name__ == "__main__":
    dates = list(generate_dates(50))

    s1 = sort(dates, 31, lambda s: s.day)
    s2 = sort(s1, 13, lambda s: s.month)
    s3 = sort(s2, 2010, lambda s: s.year)

    print(" -- Sorted random dates (counting): --")
    for v in s3:
        print(v)

    s4 = sorted(dates, key = lambda s: s.day)
    s5 = sorted(s4, key = lambda s: s.month)
    s6 = sorted(s5, key = lambda s: s.year)

    print("\n -- Sorted random dates (default): --")
    for v in s6:
        print(v)
