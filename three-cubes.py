"""
Find ways to express a number as a sum of three cubes of integers

Inspired by this Numberphile video:

"""
# Most of the solutions are pretty small, but some are huge
# To speed up the search, we do it in stages
SEARCH_MAX_A = 20
SEARCH_MAX_B = 60
SEARCH_MAX_C = 180

def simplify_cubes(cubes):
    """
    Take a triplet of cubes and try to reduce them

    For example, (-99, 3, 99) can be simplified to (0, 3, 0)
    """
    a, b, c = cubes

    if a == -b:
        return (0, 0, c)
    if a == -c:
        return (0, b, 0)
    if b == -c:
        return (a, 0, 0)
    # Couldn't simplify
    return cubes


def find_cubes_in_range(n, values):
    """
    Find three cubes that add up to n in values

    Arguments:
    n -- an integer
    values -- a list of values to check, usually generated with range()
    """
    for a in values:
        for b in values:
            for c in values:
                if a**3 + b**3 + c**3 == n:
                    return simplify_cubes((a, b, c))

    # No cubes found
    return (None, None, None)


def find_cubes(n):
    """Find three cubes of integers that add up to n"""
    # Integers of the form 9n + 4 and 9n + 5 don't work...
    if (n - 4) % 9 == 0 or (n - 5) % 9 == 0:
        return (None, None, None)
    # ...but there should be a solution for every other int
    # Calculate the ranges
    RANGE_A = range(-SEARCH_MAX_A, SEARCH_MAX_A)
    RANGE_B = range(-SEARCH_MAX_B, SEARCH_MAX_B)
    RANGE_C = range(-SEARCH_MAX_C, SEARCH_MAX_C)

    # Try the small range
    cubes = find_cubes_in_range(n, RANGE_A)

    if cubes != (None, None, None):
        return cubes

    # Try the middle range
    cubes = find_cubes_in_range(n, RANGE_B)

    if cubes != (None, None, None):
        return cubes

    # Try the big range
    return find_cubes_in_range(n, RANGE_C)


def main():
    """Get user input and look for sums of cubes"""
    print('This program will find three integers that satisfy the equation:\n')
    print('{:^80}\n'.format('a\xb3 + b\xb3 + c\xb3 = n'))
    print('For any integer n.\n')

    n = int(input('Enter an integer: '))
    cubes = find_cubes(n)

    print('')
    if cubes != (None, None, None):
        print('{0} = {1[0]}\xb3 + {1[1]}\xb3 + {1[2]}\xb3'.format(n, cubes))
    else:
        print('{0} is not expressible as the sum of three cubes.'.format(n))

if __name__ == '__main__':
    main()
