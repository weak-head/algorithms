# Cutting the rod
#  - brute-force approach in exponential time
#  - top-down memoized dynamic programming in quadratic time
#  - bottom-up dynamic programming in quadratic time


def brute_force_cut_rod(p, rod_len):
    """
    Cut rod using brute force.
    Time: O(2^n)
    Space: O(2^n)
    """
    cuts = [0] * (rod_len + 1)
    best_price = [float("-inf")] * (rod_len + 1)

    def _bf_cut(p, l):
        if l == 0:
            return 0

        for cut_at in range(1, l + 1):
            cut_price = p[cut_at] + _bf_cut(p, l - cut_at)

            if cut_price > best_price[l]:
                best_price[l] = cut_price
                cuts[l] = cut_at

        return best_price[l]

    _bf_cut(p, rod_len)
    return (cuts, best_price)


def top_down_cut_rod(p, l):
    """
    Top-down memoized dynamic programming variant
    of cut rod.
    Time: O(n^2)
    Space: O(n)
    """
    cuts = [0] * (l + 1)
    price = [float("-inf")] * (l + 1)

    def _td_cut_rod(p, l):
        if l == 0:
            return 0

        if price[l] != float("-inf"):
            return price[l]

        for cut in range(1, l + 1):
            cut_price = p[cut] + _td_cut_rod(p, l - cut)
            if cut_price > price[l]:
                price[l] = cut_price
                cuts[l] = cut
        
        return price[l]

    _td_cut_rod(p, l)
    return (cuts, price)


def bottom_up_cut_rod(p, l):
    """
    Bottom-up dynamic programming variant.
    Time: O(n^2)
    Space: O(n)
    """
    cuts = [0] * (l + 1)
    price = [float("-inf")] * (l + 1)
    price[0] = 0
    for rod_len in range(1, l+1):
        for cut in range(1, rod_len + 1):
            cut_price = p[cut] + price[rod_len - cut]
            if cut_price > price[rod_len]:
                price[rod_len] = cut_price
                cuts[rod_len] = cut
    return cuts, price


def visualize_cuts(cuts, best_price, price, rod_len):
    s = "{0} (${1}) => |".format(rod_len, best_price[rod_len])
    while rod_len > 0:
        s += " @{0} (+${1}) |".format(cuts[rod_len], price[cuts[rod_len]])
        rod_len = rod_len - cuts[rod_len]
    return s 


problem_set = [
    (10, [0, 1, 4, 5, 6, 9, 12, 17, 18, 20, 21]),
    (10, [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]),
    (18, [0, 0, 2, 3, 4, 6, 6, 5, 7, 7, 13, 13, 13, 12, 12, 13, 13, 15, 15, 17, 17, 19, 19])
]

for rod_len, price in problem_set:
    print("{0} @ {1}".format(rod_len, price))

    cuts, best_price = brute_force_cut_rod(price, rod_len)
    print("  bf: {0}".format(visualize_cuts(cuts, best_price, price, rod_len)))
    
    cuts, best_price = top_down_cut_rod(price, rod_len)
    print("  td: {0}".format(visualize_cuts(cuts, best_price, price, rod_len)))

    cuts, best_price = bottom_up_cut_rod(price, rod_len)
    print("  bu: {0}".format(visualize_cuts(cuts, best_price, price, rod_len)))

    print("")