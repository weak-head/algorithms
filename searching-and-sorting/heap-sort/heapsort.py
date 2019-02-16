
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
    a = [1,37,2,7,2,49,0,5,9,12]
    heapsort(a)
    print(a)


