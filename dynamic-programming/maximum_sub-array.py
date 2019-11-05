# Maximum sub-array


def max_sub_bf(a):
    """
    Max subarray using brute force.
    Time: O(n^2)
    Space: O(1)
    """

    lix, rix, max_sum = 0, 0, float("-inf")
    for l in range(len(a)):
        curr_sum = 0
        for r in range(l, len(a)):
            curr_sum += a[r]
            if curr_sum > max_sum:
                max_sum = curr_sum
                lix, rix = l, r
    return (lix, rix, max_sum)


def max_sub_dc(a):
    """
    Max subarray using divide and conquer.
    Time: O(n * log n)
    Space O(log n)
    """

    def _max_cross(a, i, m, j):
        left_max_sum, left_max_ix = float("-inf"), m
        cur_sum = 0
        for li in range(m, -1, -1):
            cur_sum += a[li]
            if cur_sum > left_max_sum:
                left_max_sum = cur_sum
                left_max_ix = li

        right_max_sum, right_max_ix = float("-inf"), m
        cur_sum = 0
        for ri in range(m+1, j+1):
            cur_sum += a[ri]
            if cur_sum > right_max_sum:
                right_max_sum = cur_sum
                right_max_ix = ri

        return (left_max_ix, right_max_ix, left_max_sum + right_max_sum)

    def _max_sub(a, i, j):
        if i == j:
            return (i, j, a[i])

        m = (i + j) >> 1
        left_max = _max_sub(a, i, m)
        right_max = _max_sub(a, m+1, j)
        cross_max = _max_cross(a, i, m, j)

        if left_max[2] > right_max[2] and left_max[2] > cross_max[2]:
            return left_max
        elif right_max[2] > left_max[2] and right_max[2] > cross_max[2]:
            return right_max
        else:
            return cross_max

    return _max_sub(a, 0, len(a)-1)


def max_sub_dp(a):
    """
    Max subarray using dynamic programming.
    Time: O(n)
    Space: O(n)
    """
    m = [0] * len(a)
    s = [0] * len(a)
    m[0] = a[0]
    for i in range(1, len(a)):
        contiguous_sum = m[i-1] + a[i]
        independent_sum = a[i]
        if independent_sum > contiguous_sum:
            s[i] = i
            m[i] = independent_sum
        else:
            s[i] = s[i-1]
            m[i] = contiguous_sum

    max_sum, rix = float("-inf"), 0
    for i in range(0, len(a)):
        if m[i] > max_sum:
            max_sum = m[i]
            rix = i

    return (s[rix], rix, max_sum)


def max_sub_linear(a):
    """
    Max subarray in linear time.
    Time: O(n)
    Space: O(1)
    """
    max_sum, mlix, mrix = float("-inf"), 0, 0
    current_sum, lix, rix = float("-inf"), 0, 0
    for i in range(len(a)):
        current_sum += a[i]
        rix = i
        if current_sum > max_sum:
            max_sum = current_sum
            mlix, mrix = lix, rix
        if current_sum < 0:
            current_sum = 0
            lix = rix = i+1
    return (mlix, mrix, max_sum)


ars = [
    [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7],
    [-12, -1, -2, -3, -1, -1, -7, -11],
    [-7, -2, 5, -4, 6, -8, -1],
]
for a in ars:
    print(a)
    print("   bf: {0}".format(max_sub_bf(a)))
    print("  d&c: {0}".format(max_sub_dc(a)))
    print("   dp: {0}".format(max_sub_dp(a)))
    print("  lin: {0}".format(max_sub_linear(a)))
    print()