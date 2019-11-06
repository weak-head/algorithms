# Longest common subsequence
# - brute force in exponential time
# - bottom-up dynamic programming in quadratic time
# - top-down memoized dynamic programming in quadratic time

def brute_force_lcs(a, b):
    """
    Brute force solution of LCS
    Time: O(2^(n+m))
    Space: O(2^(n+m))
    """

    def bf_lcs(x, y, xi, yi):
        if xi < 0 or yi < 0:
            return "" 
        if x[xi] == y[yi]:
            return bf_lcs(x, y, xi-1, yi-1) + x[xi] 
        else:
            l1, l2 = bf_lcs(x, y, xi-1, yi), bf_lcs(x, y, xi, yi-1)
            return l1 if len(l1) > len(l2) else l2

    return bf_lcs(a, b, len(a) - 1, len(b) - 1)

def bottom_up_lcs(a, b):
    """
    Bottom-up dynamic programming solution of LCS
    Time: O(nm)
    Space: O(nm)
    """
    al, bl = len(a) + 1, len(b) + 1
    r = [[0 for x in range(bl)] for y in range(al)]
    d = [[None for x in range(bl)] for y in range(al)]

    for i in range(1, al):
        for j in range(1, bl):
            if a[i-1] == b[j-1]:
                r[i][j] = r[i-1][j-1] + 1
                d[i][j] = "diagonal"
            elif r[i-1][j] >= r[i][j-1]:
                r[i][j] = r[i-1][j]
                d[i][j] = "up"
            else:
                r[i][j] = r[i][j-1]
                d[i][j] = "left"

    return (r, d)


def top_down_lcs(a, b):
    """
    Top-down memoized dynamic programming solution of LCS
    Time: O(nm)
    Space: O(nm)
    """
    al, bl = len(a), len(b)
    r = [[float("-inf") for y in range(bl + 1)] for x in range(al + 1)]

    for i in range(0, len(a)):
        r[i][0] = 0

    for j in range(0, len(b)):
        r[0][j] = 0

    def td_lcs(a, b, i, j):
        if i == 0 or j == 0:
            return 0

        if r[i][j] == float("-inf"):
            if a[i-1] == b[j-1]:
                v = td_lcs(a, b, i-1, j-1)
                r[i][j] = v + 1
            else:
                v1 = td_lcs(a, b, i-1, j)
                v2 = td_lcs(a, b, i, j-1)
                r[i][j] = v1 if v1 > v2 else v2

        return r[i][j]


    td_lcs(a, b, al, bl)
    return r


def recover_lcs_d(d, a, i, j):
    """
    Recover the LCS from the composed matrix of directions.
    Time: O(n)
    Space: O(n)
    """
    if i == 0 or j == 0:
        return ""

    if d[i][j] == "diagonal":
        s = recover_lcs_d(d, a, i-1, j-1)
        return s + a[i-1]
    elif d[i][j] == "up":
        return recover_lcs_d(d, a, i-1, j)
    else:
        return recover_lcs_d(d, a, i, j-1)


def recover_lcs_r(r, a, b, i, j):
    """
    Recover the LCS from the resulting length matrix.
    Time: O(n)
    Space: O(n)
    """
    if i == 0 or j == 0:
        return ""

    if a[i-1] == b[j-1]:
        s = recover_lcs_r(r, a, b, i-1, j-1)
        return s + a[i-1]
    elif r[i-1][j] >= r[i][j-1]:
        return recover_lcs_r(r, a, b, i-1, j)
    else:
        return recover_lcs_r(r, a, b, i, j-1)


pairs = [
    ("abcdfsj", "aceeeeeedk"),
    ("abcbdab", "bdcba"),
    ("abcde", "kfl"),
    ("abc", ""),
    ("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA", "GTCGTTCGGAATGCCGTTGCTCTGTAAA"),
]


for a, b in pairs:

    # Naive brute force approach
    if len(a) <= 8 or len(b) <= 8:
        lcs1 = brute_force_lcs(a, b)
    else:
        lcs1 = "-"

    # Bottom-up
    r, d = bottom_up_lcs(a, b)
    lcs2 = recover_lcs_d(d, a, len(a), len(b))
    lcs2 = recover_lcs_r(r, a, b, len(a), len(b))

    # Top-down with memoization
    r = top_down_lcs(a, b)
    lcs3 = recover_lcs_r(r, a, b, len(a), len(b))

    print("{0} <-> {1}".format(a, b))
    print("    BF: [{0}]".format(lcs1))
    print("    TD: [{0}]".format(lcs2))
    print("    BU: [{0}]".format(lcs3))