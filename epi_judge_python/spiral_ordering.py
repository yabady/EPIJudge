from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:

    spiral = []
    t, r, b, l = 0, len(square_matrix)-1, len(square_matrix)-1, 0
    d = 0  # 1= t-r, 2=r-b, 3=b-l, 4=t-l

    while (t <= b and l <= r):

        if d == 0:
            for i in range(l, r+1):
                spiral.append(square_matrix[t][i])
            t += 1

        elif d == 1:
            for i in range(t, b+1):
                spiral.append(square_matrix[i][r])
            r -= 1

        elif d == 2:
            for i in range(r, l-1, -1):
                spiral.append(square_matrix[b][i])
            b -= 1

        elif d == 3:
            for i in range(b, t-1, -1):
                spiral.append(square_matrix[i][l])
            l += 1

        d = (d + 1) % 4
    return spiral


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
