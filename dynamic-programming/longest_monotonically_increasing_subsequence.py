# Longest monotonically increasing subsequence
# - brute force in exponential time
# - bottom up, similar to LCS
# - bottom up that builds internal chains
# - bottom up in O(n * log n)

from bisect import bisect_left

def brute_force_lmis(a):
    """
    Brute force solution.
    Time: O(2^n)
    Space: O(2^n)
    """

    def _bf_lmis(a, p, aix):
        max_chain = ""

        for j in range(aix, len(a)):
            if p is None or a[j] > p:
                chain = a[j] + _bf_lmis(a, a[j], j+1)
                if len(chain) > len(max_chain):
                    max_chain = chain

        return max_chain

    return _bf_lmis(a, None, 0)


def bottom_up_lcs_lmis(a):
    """
    Bottom-up dynamic programming variant that
    uses approach similar to the Longest Common Subsequence.
    Time: O(n^2)
    Space: O(n^2)
    """

    def recover_lcs(d, a, i, j):
        """
        Recover the LCS from the composed matrix of directions.
        Time: O(n)
        Space: O(n)
        """
        if i == 0 or j == 0:
            return ""

        if d[i][j] == "diagonal":
            s = recover_lcs(d, a, i-1, j-1)
            return s + a[i-1]
        elif d[i][j] == "up":
            return recover_lcs(d, a, i-1, j)
        else:
            return recover_lcs(d, a, i, j-1)

    b = "".join(sorted(a))
    ln = [[0 for x in range(len(a) + 1)] for y in range(len(a) + 1)]
    ix = [[None for x in range(len(a) + 1)] for y in range(len(a) + 1)]

    for j in range(1, len(a) + 1):
        for i in range(1, len(a) + 1):
            # current characters in both strings are equal 
            # and the current character in any of these strings
            # doesn't equal to previous character in the other string
            # (avoid repeating characters)
            if a[i-1] == b[j-1] and a[i-1] != b[j-2] and a[i-2] != b[j-1]:
                ln[j][i] = ln[j-1][i-1] + 1
                ix[j][i] = "diagonal"
            elif ln[j-1][i] >= ln[j][i-1]:
                ln[j][i] = ln[j-1][i]
                ix[j][i] = "up"
            else:
                ln[j][i] = ln[j][i-1]
                ix[j][i] = "left"

    return recover_lcs(ix, b, len(a), len(a)) 


def bottom_up_lmis(a):
    """
    Bottom-up dynamic programming variant that
    builds internal chains of sequences.
    Time: O(n^2)
    Space: O(n)
    """
    ln = [1] * len(a) # chain len
    ix = [None] * len(a) # previous ix

    # build internal chains
    for j in range(len(a)):
        for pix in range(j):
            if a[pix] < a[j]:
                if ln[pix] + 1 > ln[j]:
                    ln[j] = ln[pix] + 1
                    ix[j] = pix

    # find end ix of the longest chain and it's length
    max_ix, max_len = 0, 0
    for j in range(len(a)):
        if ln[j] > max_len:
            max_len = ln[j]
            max_ix = j

    # recover the chain
    cix, chain = max_ix, ""
    while cix != None:
        chain = a[cix] + chain
        cix = ix[cix]
    
    return chain


def quick_lmis_len(a):
    """
    Get the length of the longest increasing sequence
    in O(n * log n).
    Additional references: 
        https://en.wikipedia.org/wiki/Patience_sorting
        https://en.wikipedia.org/wiki/Longest_increasing_subsequence
    """
    tails = []
    for c in a:
        i = bisect_left(tails, c)
        if i == len(tails):
            tails.append(c)
        tails[i] = c
    return len(tails) 


def quick_lmis(a):
    """
    Get the longest increasing sequence using
    variant of Patience sorting.
    Time: O(n * log n)
    Space: O(n)
    Additional references: 
        https://en.wikipedia.org/wiki/Patience_sorting
        https://en.wikipedia.org/wiki/Longest_increasing_subsequence
    """

    class Node:
        def __init__(self, v, next=None):
            self.v = v
            self.next = next
        def __lt__(self, other):
            if type(other) is str:
                return self.v < other
            return self.v < other.v
        
    def deep_copy(node):
        if node is None:
            return None
        return Node(node.v, deep_copy(node.next))

    def assemble(node):
        if node is None:
            return ""
        return assemble(node.next) + node.v 

    tails = []
    for c in a:
        i = bisect_left(tails, c)
        if i == len(tails):
            last = deep_copy(tails[-1]) if tails != [] else None
            tails.append(Node(c, last))
        tails[i].v = c

    return assemble(tails[-1]) 


sequences = [
    "2849713580",
    "1043276980",
    "192834756",
    "0a1b2z3r4k5v6a7b8a9",
    "dynamicprogramming",
    "longestincreasingsequence",
    "mathematicaloptimizationmethod",
]

for seq in sequences:

    ln1 = quick_lmis_len(seq)
    bf1 = brute_force_lmis(seq)
    bu1 = bottom_up_lmis(seq)
    bu2 = bottom_up_lcs_lmis(seq)
    qk1 = quick_lmis(seq)

    print("{0}:".format(seq)) 
    print("     len: {0}".format(ln1))
    print("      bf: {0}".format(bf1))
    print("      bu: {0}".format(bu1))
    print("  bu_lcs: {0}".format(bu2))
    print("   quick: {0}".format(qk1))
    print("")