from typing import List

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
    arr = [72,1,23,19,3,57,12,2,94,37,42,24]
    shell_sort(arr)
    print(arr)