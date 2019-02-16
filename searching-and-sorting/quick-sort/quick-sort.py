
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
    arr = [0, 7, 11, 23, 4, 2, 1, 5, 19, 7]
    quick_sort(arr)
    print(arr)
