"""Find all the Keith numbers in a given range and attempt to cluster them."""
import argparse


def get_digits(value):
    """Return a list containg the digits of the given integer."""
    digits = []
    for d in str(value):
        digits.append(int(d))
    return digits


def is_keith(value, showSteps=False):
    """Check whether the given number is a Keith number."""
    digits = get_digits(value)
    values = digits[1:len(digits)]
    s = sum(digits)
    values.append(s)

    if showSteps:
        print('{0:s} = {1}'.format(' + '.join([str(v) for v in digits]), s))
    while s < value:
        s = sum(values)
        if showSteps:
            print('{0:s} = {1}'.format(' + '.join([str(v) for v in values]), s))
        values.append(s)
        values.pop(0)
    return s == value

parser = argparse.ArgumentParser()
parser.add_argument('-m',
                    '--maxvalue',
                    help='The value to stop searching for Keith numbers at.',
                    type=int,
                    default=0)
parser.add_argument('-q',
                    '--quiet',
                    help='Don\'t show information about Keith numbers or the steps involved in verifying them.',
                    action='store_true',
                    default=False)
args = parser.parse_args()

if not args.quiet:
    # Explain Keith numbers to the user
    print("A Keith number is any n-digit integer where repeatedly summing groups")
    print("of n numbers from the digits and then the resulting sums yields the")
    print("original number.\n")
    print("For example, 14 is a Keith number because 1 + 4 = 5, 4 + 5 = 9, and")
    print("5 + 9 = 14.\n")
    print("A Keith cluster is any group of Keith numbers that are multiples of")
    print("the smallest member of the cluster.\n")
    print("This script will search for Keith numbers and Keith clusters up to")
    print("the given upper bound.\n\n")

if args.maxvalue == 0:
    # Get the upper bound for our search
    try:
        keithMax = int(input('Enter the number to stop searching at: '))
    except:
        print('Invalid input.')
        quit()
else:
    keithMax = args.maxvalue

showSteps = not args.quiet

# Look for Keith numbers between 10 and keithMax (all single-digit integers are Keith numbers)
keiths = []
for k in range(10, keithMax):
    if is_keith(k):
        keiths.append(k)
        print('{0} is a Keith number.'.format(k))
        if showSteps:
            is_keith(k, True)
            print('')

# Look for Keith clusters (all cluster members are integer multiples of the smallest member and have the same number of digits)
clusters = {}
for k0 in keiths:
    k0digits = len(get_digits(k0))
    for k in keiths:
        if k != k0 and k % k0 == 0 and len(get_digits(k)) == k0digits:
            if k0 in clusters:
                clusters[k0].append(k)
            else:
                clusters[k0] = [k0, k]
# Did we find any clusters?
if len(clusters) > 0:
    print('\nFound {0} Keith clusters.'.format(len(clusters)))
    for c in clusters:
        print('Multiples of {0}: {1}'.format(c, str(clusters[c])))
else:
    print('\nNo Keith clusters found.')
