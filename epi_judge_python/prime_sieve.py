from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    result = []
    # We are going to use the canidete approuch where we will store already itrated primes and update later on tog et faster solution
    primes = [False, False] + [True] * (n-1)

    for i in range(n+1):
        if primes[i]:
            result.append(i)
            for j in range(i, n+1, i):

                primes[j] = False

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
