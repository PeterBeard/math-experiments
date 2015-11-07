# Find happy numbers -- numbers where repeatedly squaring and summing its digits will lead to 1
#     e.g. 7 is happy because
#		7^2 = 49
#		4^2 + 9^2 = 97
#		9^2 + 7^2 = 130
#		1^2 + 3^2 + 0^2 = 10
#		1^2 + 0^2 = 1
from math import log

# Calculate the sum of the squares of the digits in number
def squareDigits(number,showSteps=False):
	decimated_value = number
	# Values with one digit are easy
	if decimated_value < 10:
		return decimated_value ** 2
	# More than one digit is a bit trickier
	# Log base 10 tells us how many digits the number has (minus 1)
	magnitude = int(log(decimated_value, 10))
	# Square the first digit and recurse over the rest
	first_digit = int(decimated_value / (10**magnitude))
	return first_digit**2 + squareDigits((decimated_value - first_digit*(10**magnitude)), showSteps)

# Determine whether a number is happy by summing the squares of its digits and repeating with the sum
def isHappy(number,showSteps=True):
	usedValues = []
	digitsum = number
	# Keep calculating until we get to 1
	while digitsum != 1:
		usedValues.append(digitsum)
		if showSteps:
			print digitsum, "=>",
		digitsum = squareDigits(digitsum,showSteps)
		if showSteps:
			print digitsum
		# If numbers start to repeat then we CANNOT reach 1; this is not a happy number :(
		if digitsum in usedValues:
			return 0
	# We made it to 1; must be a happy number :)
	return 1

# Get a number from the user and determine whether it's a happy number
def userNumber():
	try:
		number = int(raw_input("Enter a positive integer: "))
	except:
		print "You have failed to enter an integer. Well done."
		quit()

	if isHappy(number):
		print number, "is a happy number :)"
	else:
		print number, "is not a happy number :("

# Search for happy numbers between the boundaries given by the user
def findHappyNumbers():
	try:
		startValue = int(raw_input("Start search at:"))
	except:
		print "Error parsing input."
		return
	try:
		endValue = int(raw_input("Stop search at:"))
	except:
		print "Error parsing input."
		return
	
	happies = []
	for i in range(startValue,endValue+1):
		if isHappy(i,False):
			happies.append(str(i))
	
	print ', '.join(happies), "are happy numbers :)"

print 'A happy number is any number where repeatedly squaring and summing the'
print 'digits will eventually give the number 1.'
print ''
print 'For example, 13 is a happy number because:'
print '1^2 + 3^2 = 10'
print '1^2 + 0^2 = 1'
print ''
print 'This script will find happy numbers in the given range.'
print ''

findHappyNumbers()
