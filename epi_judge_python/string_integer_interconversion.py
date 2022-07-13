from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
<<<<<<< HEAD
    neg = False
    res = []

    if x < 0:
        neg = True
        x = -x

    elif x == 0:
        return "0"

    while x:
        res.append(chr(x % 10 + ord("0")))
        x = x // 10

    if neg:
        return "-" + "".join(res[::-1])
    else:
        return "".join(res[::-1])


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    res = 0
    neg = False

    if s[0] == '+':
        s = s[1:]
    elif s[0] == "-":
        s = s[1:]
        neg = True

    if s[0] == 0:
        return 0
        
    for i in range(len(s)):

        if s[0] == "-":
            neg = True
            continue
        res = res * 10 + (ord(s[i]) - ord("0"))
=======

    neg = False
    res = []

    if x == 0:
        return "0"
    elif x < 0:
        neg = True
        x = -x

    # -123
    # 123 neg = True

    while x:

        last_digit = x % 10
        # chr() int --> string
        # ord() string --> int
        str_last_digit = chr(last_digit + ord("0"))
        res.append(str_last_digit)
        x = x // 10

    # ['3','2','1']

    if neg:
        res.append("-")

    # ['3','2','1','-']

    return "".join(res[::-1])


def string_to_int(s: str) -> int:
    
    # "-123"
    neg = False
    res = 0

    if s[0] == "-":
        neg = True
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]

    if s[0] == 0:
        return 0

    # "123" neg = True

    for i in range(len(s)):

        #
        digit = ord(s[i]) - ord("0")
        res = res * 10 + digit
>>>>>>> a6dec57d848e26e00a2d250d2262bd1d2f0860ee

    if neg:
        res = -res

    return res


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
