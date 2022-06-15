from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # [1,2,9] --> [1,3,0], [9,9,9] --> [1,0,0,0]

    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] % 10 != 0:
            break
        A[i] = 0
        A[i - 1] += 1

    if A[0] % 10 == 0:
        A[0] = 1
        A.append(0)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
