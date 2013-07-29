# Find all the Keith numbers in a given range and attempt to cluster them
import argparse

# Return a list containng the digits of the given integer
def getDigits(value):
	digits = []
	for d in str(value):
		digits.append(int(d))
	return digits

# Check whether the given number is a Keith number
def isKeith(value, showSteps=False):
	digits = getDigits(value)
	values = digits[0:len(digits)]
	s = sum(digits)
	if showSteps:
		print '  ' + ' + '.join(str(x) for x in values) + ' = ' + str(s)
	values.append(s)
	while s < value:
		values.pop(0)
		s = sum(values)
		if showSteps:
			print '  ' + ' + '.join(str(x) for x in values) + ' = ' + str(s)
		values.append(s)
	return s == value
parser = argparse.ArgumentParser()
parser.add_argument('-m','--maxvalue',help='The value to stop searching for Keith numbers at.', type=int, default=0)
parser.add_argument('-q','--quiet',help='Don\'t show information about Keith numbers or the steps involved in verifying them.', action='store_true', default=False)
args = parser.parse_args()

if not args.quiet:
	# Explain Keith numbers to the user
	print "A Keith number is any n-digit integer where repeatedly summing groups"
	print "of n numbers from the digits and then the resulting sums that results"
	print "in the original number."
	print
	print "For example, 14 is a Keith number because 1 + 4 = 5, 4 + 5 = 9, and"
	print "5 + 9 = 14."
	print
	print "A Keith cluster is any group of Keith numbers that are multiples of"
	print "the smallest member of the cluster."
	print
	print "This script will search for Keith numbers and Keith clusters up to"
	print "the given upper bound."
	print
	print

if args.maxvalue == 0:
	# Get the upper bound for our search
	try:
		keithMax = int(raw_input('Enter the number to stop searching at: '))
	except:
		print 'Invalid input.'
		quit()
else:
	keithMax = args.maxvalue

showSteps = not args.quiet

# Look for Keith numbers between 10 and keithMax (all single-digit integers are Keith numbers)
keiths = []
for k in range(10,keithMax):
	if isKeith(k):
		keiths.append(k)
		print k, 'is a Keith number.'
		if showSteps:
			isKeith(k,True)
			print

# Look for Keith clusters (all cluster members are integer multiples of the smallest member and have the same number of digits)
clusters = {}
for k0 in keiths:
	k0digits = len(getDigits(k0))
	for k in keiths:
		if k != k0 and k % k0 == 0 and len(getDigits(k)) == k0digits:
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

