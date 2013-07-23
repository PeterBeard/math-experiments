def getDigits(value):
	digits = []
	for d in str(value):
		digits.append(int(d))
	return digits

def isKeith(value, showSteps=False):
	digits = getDigits(value)
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

try:
	keithMax = int(raw_input('Enter the number to stop searching at: '))
except:
	print 'Invalid input.'

# Look for Keith numbers between 10 and keithMax
keiths = []
for k in range(10,keithMax):
	if isKeith(k):
		keiths.append(k)
		print k, 'is a Keith number.'

# Look for Keith clusters (all cluster members are integer multiples of the smallest member)
clusters = {}
for k0 in keiths:
	k0digits = len(getDigits(k0))
	for k in keiths:
		if k != k0 and k % k0 == 0 and len(getDigits(k)) == k0digits:
			if k0 in clusters:
				clusters[k0].append(k)
			else:
				clusters[k0] = [k0, k]
print
if len(clusters) > 0:
	print 'Found', len(clusters), 'Keith clusters.'
	for c in clusters:
		print 'Multiples of',c,':',clusters[c]
else:
	print 'No Keith clusters found.'

