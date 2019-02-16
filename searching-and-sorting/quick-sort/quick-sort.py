
def quick_sort(a):
    pass

def quick_sort(a, l, r):
    pass

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
    if (l >= r):
        return

    last_min, pivot = l, a[r]
    for i in range(l, r):
        if (a[i] <= pivot):
           a[i], a[last_min] = a[last_min], a[i]
           last_min += 1

    a[last_min], a[r] = a[r], a[last_min]

    return last_min


if __name__ == '__main__':
    print(partition([0, 7, 11, 23, 4, 2, 1, 5, 19, 7], 0, 9))
