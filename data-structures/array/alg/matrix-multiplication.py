def multiply(ma, mb):
    z = [[0 for r in range(len(mb[0]))] for c in range(len(ma))]

    for i in range(len(ma)):
        for j in range(len(mb[0])):
            for m in range(len(mb)):
                print('z[', i, '][', j, '] += ', ma[i][m], 'x', mb[m][j])
                z[i][j] += ma[i][m] * mb[m][j]
    return z

if __name__ == '__main__':
    a = [ [1, 2]
        , [3, 4]
        , [5, 6]
        , [6, 7] ]

    b = [ [1, 2, 3]
        , [4, 5, 6] ]

    z = multiply(a, b)
    print(z)
    print('\n')

    c = [ [4, 2, 4]
        , [8, 3, 1] ]

    d = [ [3, 5]
        , [2, 8]
        , [7, 9] ]

    z = multiply(c, d)
    print(z)
    print('\n')

    e = [ [2, 1, 4]
        , [0, 1, 1] ]

    f = [ [6, 3, -1, 0]
        , [1, 1, 0, 4]
        , [-2, 5, 0, 2] ]

    z = multiply(e, f)
    print(z)