from asyncore import write
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    real_index, a_count = 0,0
    for i in range(size):
        if s[i] != "b":
            s[real_index] = s[i]
            real_index += 1
        if s[i] == 'a':
            a_count += 1

    print(size)
    print(real_index)
    print(s)
    print(a_count)
    print("testrtt")


    return 0


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
