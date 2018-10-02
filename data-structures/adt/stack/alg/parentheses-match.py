'''
Determine whether the parentheses in a string are
balanced and properly nested.
'''

class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def isEmpty(self):
        return len(self.__stack) == 0

def balanced(expression):
    stack = Stack()
    parens = { ')':'(',']':'[','}':'{'}
    open_parens = parens.values()
    close_parens = parens.keys()
    for ix, c in enumerate(expression):
        if c in open_parens:
            stack.push((c, ix))
        elif c in close_parens:
            (cp, ixo) = stack.pop()
            if parens.get(c) != cp:
                return (False, ix)
    if stack.isEmpty():
        return (True, 0)
    else:
        (_, ixo) = stack.pop()
        return (False, ixo)

if __name__ == '__main__':
    print(balanced('(())('))
    print(balanced('[{}()[]]'))
