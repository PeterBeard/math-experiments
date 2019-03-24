# -*- coding: utf-8 -*-
"""
Check the multiplicative persistence of a number
"""
import argparse
import operator


def multiply_digits(n):
    """
    Multiply together the digits of a number
    """
    digits = str(n)
    product = reduce(operator.mul, map(int, digits), 1)
    return product


def get_persistence_chain(n):
    """
    Create a multiplicative persistence chain for the given number
    """
    chain = [n]
    while chain[-1] > 9:
        chain.append(multiply_digits(chain[-1]))
    return chain


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'n',
        type=int,
        help='The number to check'
    )
    args = parser.parse_args()
    n = args.n
    chain = get_persistence_chain(n)
    chain_string = ' →  '.join(map(str, chain))
    print(chain_string)
    # n doesn't count as part of the chain
    chain.pop(0)
    print('The multiplicative persistence of {} is {}'.format(n, len(chain)))


if __name__ == '__main__':
    main()
