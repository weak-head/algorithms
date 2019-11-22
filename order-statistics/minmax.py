# Minmax in linear time

def minmax(a):
    """ 3 * (n / 2) comparisons """
    minv, maxv = a[0], a[0]
    start_index = 0 if len(a) % 2 == 0 else 1
    for i in range(start_index, len(a), 2):
        if a[i] > a[i+1]:
            maxv = max(maxv, a[i])
            minv = min(minv, a[i+1])
        else:
            maxv = max(maxv, a[i+1])
            minv = min(minv, a[i])
    return minv, maxv

if __name__ == "__main__":
    a = [2,3,4,5,6,7,8,9,1]
    b = [2,3,4,5,6,7,9,1]
    print(minmax(a))
    print(minmax(b))