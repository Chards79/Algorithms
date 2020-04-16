#!/usr/bin/python

import argparse


def find_max_profit(prices):
    for i in range(0, len(prices) - 1):
        cur_index = i
        current_min_price_so_far = cur_index
    for j in range(0, len(prices))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
    # Take a list of numbers and find the smallest number
    # Then find the largest number to come after that smallest number
    # Subtract the smaller number from the larger to find the difference(profit)
    # Compare those differences(profits) as you continue through the list
    # Once you get through the whole list you should have the biggest difference comparison which you will then output
