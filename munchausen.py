# Look for Munchausen numbers
# A Munchausen number is an integer such that the sum of the digits raised to the power of themselves equals the number
# For example, 3435 is a Munchausen number because 3^3 + 4^4 + 3^3 + 5^5 = 3435

# Get the digits of an integer
def get_digits(n):
	s = str(n)
	digits = []
	for digit in s:
		digits.append(int(digit))
	return digits

# Determine whether n is a Munchausen number
def is_munchausen(n, show_steps=False):
	digits = get_digits(n)
	s = 0
	for d in digits:
		# Assume 0^0 = 0; this is common in this area according to Wikipedia
		if d > 0:
			s += d**d
	if show_steps:
		steps = []
		for d in digits:
			steps.append('%i^%i' % (d,d))
		print '%i = %s' % (n, ' + '.join(steps))
	# If the sum of d**d equals the number, it's a Munchausen number
	return s == i

# Ask the user for the parameters of the search space
try:
	lower_bound = int(raw_input('Where shall I start the search? '))
except:
	print 'Start point must be an integer.'
	quit()

try:
	upper_bound = int(raw_input('And where shall I end it? '))
except:
	print 'End point must be an integer.'
	quit()

# Look for Munchausen numbers
print 'Searching for Munchausen numbers between %i and %i.' % (lower_bound, upper_bound)
for i in xrange(lower_bound, upper_bound+1):
	if is_munchausen(i):
		is_munchausen(i, True)	

