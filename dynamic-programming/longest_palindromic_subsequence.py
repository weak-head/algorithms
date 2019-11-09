# Longest palindromic subsequence
# - brute force in exponential time
# - naive in cubic time
# - bottom up dynamic programming in quadratic time
# - top down dynamic programming with memoization
# - bottom up dynamic programming in quadratic time, linear space

def bottom_up_lps(s):
    """
    Bottom up dynamic programming variant
    of the longest palindromic subsequence.
    Time: O(n^2)
    Space: O(n^2)
    """

    L = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        L[i][i] = 1

    for substring_length in range(2, len(s) + 1):
        for row in range(len(s) - substring_length + 1):
            column = row + substring_length - 1
            
            if s[row] == s[column] and substring_length == 2:
                L[row][column] = 2
            elif s[row] == s[column]:
                L[row][column] = L[row+1][column-1] + 2
            else:
                L[row][column] = max(L[row][column-1], L[row+1][column])

    return L[0][len(s) - 1]


print(bottom_up_lps("character"))