import functools
from re import S

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start += 1
            finish -= 1

    reverse_range(s, 0, len(s)-1)

    space_idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            reverse_range(s, space_idx, i-1)
            space_idx = i + 1

        if i == len(s)-1:
            reverse_range(s, space_idx, i)
        


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
