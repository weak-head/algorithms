# Matrix-chain multiplication
# - basic matrix multiplication in cubic time
# - brute force approach in exponential time
# - top-down memoized dynamic programming approach in cubic time
# - bottom-up dynamic programming approach in cubic time

def mul(a, b):
    """
    Multiply two matrixes 'a' (n x k) and 'b' (k x m) and
    returns a matrix product (n x m)
    Time: O(nkm)
    Space: O(nm)
    """
    n, k, m = len(a), len(b), len(b[0])

    matrix = [[0 for x in range(m)] for y in range(n)]

    for c in range(n):
        for r in range(m):
            for kix in range(k):
                matrix[c][r] += a[c][kix] * b[kix][r]

    return matrix


def brute_force_chain(p):
    """
    Naive brute force variant of the matrix-chain multiplication.
    Time: O(2^n)
    Space: O(2^n)
    """

    def _bf_chain(p, s, m, i, j):
        if i == j:
            return 0

        for k in range(i, j):
            mul_value = p[i-1] * p[k] * p[j]
            total_value = (
                _bf_chain(p, s, m, i, k) +
                _bf_chain(p, s, m, k + 1, j) +
                mul_value
            )

            if total_value < m[i][j]:
                m[i][j] = total_value
                s[i][j] = k

        return m[i][j]

    matrix_cnt = len(p)
    m = [[float("inf") for r in range(matrix_cnt)] for c in range(matrix_cnt)]
    s = [[float("inf") for r in range(matrix_cnt)] for c in range(matrix_cnt)]

    _bf_chain(p, s, m, 1, matrix_cnt - 1)

    return (m, s)


def top_down_memoized_chain(p):
    """
    Top-down memoized dynamic programming variant of
    the matrix-chain multiplication.
    Time: O(n^3)
    Space: O(n^2)
    """

    def _memo_chain(p, s, m, i, j):
        if m[i][j] != float("inf"):
            return m[i][j]

        if i == j:
            m[i][j] = 0
        else:
            for k in range(i, j):
                mul_value = p[i-1] * p[k] * p[j]
                total_value = (
                    _memo_chain(p, s, m, i, k) +
                    _memo_chain(p, s, m, k + 1, j) +
                    mul_value
                )

                if total_value < m[i][j]:
                    m[i][j] = total_value
                    s[i][j] = k

        return m[i][j]

    matrix_cnt = len(p)
    m = [[float("inf") for r in range(matrix_cnt)] for c in range(matrix_cnt)]
    s = [[float("inf") for r in range(matrix_cnt)] for c in range(matrix_cnt)]

    _memo_chain(p, s, m, 1, matrix_cnt - 1)

    return (m, s)


def bottom_up_chain(p):
    """
    Evaluates optimal matrix multiplication order using dynamic programming.
    (basically the optimal binary tree)
    Time: O(n^3)
    Space: O(n^2)
    """

    matrix_cnt = len(p)
    r = [[float("inf") for x in range(matrix_cnt)] for y in range(matrix_cnt)]
    s = [[float("inf") for x in range(matrix_cnt)] for y in range(matrix_cnt)]

    for ix in range(1, matrix_cnt):
        r[ix][ix] = 0

    for combination_length in range(2, matrix_cnt):
        for row in range(1, matrix_cnt - combination_length + 1):
            column = row + combination_length - 1
            for k in range(row, column):
                mul_value = p[row-1] * p[k] * p[column]
                total_value = r[row][k] + r[k + 1][column] + mul_value
                if total_value < r[row][column]:
                    r[row][column] = total_value
                    s[row][column] = k
    return (r, s)


def visualize_optimal_parens(p, s, i, j):
    """
    Returns a string that visualizes the optimal solution.
    Time: O(n)
    Space: O(n)  (recursive calls via stack)
    """
    if i == j:
        return "{0}x{1}".format(p[i-1], p[i])
    else:
        fst = visualize_optimal_parens(p, s, i, s[i][j])
        snd = visualize_optimal_parens(p, s, s[i][j] + 1, j)
        return "({0} * {1})".format(fst, snd)


p = [30,35,15,5,10,20,25]
matrix_cnt = len(p) - 1

r1, s1 = brute_force_chain(p)
r2, s2 = top_down_memoized_chain(p)
r3, s3 = bottom_up_chain(p)

print(r1[1][matrix_cnt], "-> ", visualize_optimal_parens(p, s1, 1, matrix_cnt))
print(r2[1][matrix_cnt], "-> ", visualize_optimal_parens(p, s2, 1, matrix_cnt))
print(r3[1][matrix_cnt], "-> ", visualize_optimal_parens(p, s3, 1, matrix_cnt))
