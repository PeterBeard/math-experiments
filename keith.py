"""Find all the Keith numbers in a given range and attempt to cluster them."""


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
    while s < value:
        s = sum(values)
        if showSteps:
            print 'sum(',values, ') =', s
        values.append(s)
        values.pop(0)
    return s == value

# Get the upper bound for our search
try:
    keithMax = int(raw_input('Enter the number to stop searching at: '))
except:
        print 'Invalid input.'

# Look for Keith numbers between 10 and keithMax (all single-digit integers are Keith numbers)
keiths = []
for k in range(10,keithMax):
    if is_keith(k):
        keiths.append(k)
        print k, 'is a Keith number.'

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
print
if len(clusters) > 0:
    print 'Found', len(clusters), 'Keith clusters.'
    for c in clusters:
        print 'Multiples of',c,':',clusters[c]
else:
    print 'No Keith clusters found.'

