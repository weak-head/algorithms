import sys


def dist(a, b):
    """Evaluates a distance between two points."""
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5


def nearest(base, lst):
    """Gets the nearest point to the base."""
    min_n, min_d = None, sys.maxsize
    for y in lst:
        d = dist(base, y)
        if d < min_d:
            min_n, min_d = y, d
    return min_n


def nearest_neighbor(lst):
    """Builds the TSP path using the nearest neighbor heuristic."""
    if not lst:
        raise StopIteration
    x, n_lst = lst[0], lst[1:]
    yield x
    while n_lst:
        x = nearest(x, n_lst)
        n_lst.remove(x)
        yield x


bad_ex = [(0, 0),
          (0, 1),
          (0, -1),
          (0, 3),
          (0, -5),
          (0, 11),
          (0, 21)]


good_ex = [(0, 50),
           (25, 75),
           (50, 100),
           (75, 75),
           (100, 50),
           (75, 25),
           (50, 0),
           (25, 25)]
