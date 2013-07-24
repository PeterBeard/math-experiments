# Find happy numbers -- numbers where repeatedly squaring and summing its digits will lead to 1
#     e.g. 7 is happy because
#		7^2 = 49
#		4^2 + 9^2 = 97
#		9^2 + 7^2 = 130
#		1^2 + 3^2 + 0^2 = 10
#		1^2 + 0^2 = 1

# Calculate the sum of the squares of the digits in number
def squareDigits(number,showSteps=False):
	squaresum = 0
	digits = []
	steps = []
	for d in str(number):
		square = int(d)**2
		digits.append(d + '^2')
		steps.append(square)
		squaresum += square

	if showSteps:
		print ' + '.join(digits), '=',
	
	return squaresum

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

findHappyNumbers()
