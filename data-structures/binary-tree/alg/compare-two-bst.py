
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)

def compare_two_bst(fst: Node, snd: Node):
    fst_data = fst.data if fst else None
    snd_data = snd.data if snd else None

    if fst is None and snd is None:
        return True

    if fst_data == snd_data:
        l_comp = compare_two_bst(fst.left, snd.left)
        r_comp = compare_two_bst(fst.right, snd.right)
        return l_comp and r_comp

    return False

if __name__ == '__main__':
    expectation = [
        (None, None, True),
        (Node(1), None, False),
        (Node(4), Node(4), True),
        (Node(4, Node(2)), Node(4, right=Node(6)), False),
        (Node(4, Node(2)), Node(4, Node(6)), False),
        (Node(4, Node(1)), Node(4, Node(1)), True)
    ]

    for (f, s, r) in expectation:
        if compare_two_bst(f, s) != r:
            print('Failed on {} vs {}'.format(f, s))

    print('done')