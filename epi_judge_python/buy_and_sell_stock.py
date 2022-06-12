from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # [ 50, 40, 30, 50, 20, 100, 10, 50] --> 80
    # O(n) constant amount of work in array
    # O(1) space since we are tracking the iterator, profit, and lowest vars

    profit = 0
    lowest = float('inf')

    for price in prices:
        if price < lowest:
            lowest = price
        
        profit = max(profit, price-lowest)

    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
