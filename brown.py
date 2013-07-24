# Guess a number chosen by the user using a clever trick
import math

# Generate a stack of cards given the indices of the cards and the largest number to be represented
def generateCards(indices, limit):
	ncards = len(indices)
	indices = sorted(indices)[::-1]
	if limit > sum(indices):
		print "Cannot generate enough cards using the given indices."
		return []
	cards = []
	for i in range(0,ncards):
		cards.append([])
	for n in range(1,limit+1):
		# Figure out which cards need to have n on them
		appearsOn = []
		nt = n
		for i in range(0,ncards):
			if nt >= indices[i]:
				nt -= indices[i]
				appearsOn.append(i)
		# Add the number to the correct cards
		for c in appearsOn:
			cards[c].append(n)
	return cards

# Display the card in a pleasing way
def displayCard(card):
	nitems = len(card)
	displaysize = int(math.sqrt(nitems))+1

	for i in range(0,displaysize):
		for j in range(0,displaysize):
			index = j+i*displaysize
			if index < nitems:
				print card[index],
		print


cards = generateCards([1,2,3,5,8,13],30)

s = raw_input('Think of a number between 1 and 30. Press enter when you have a number.')
# The players number is just the sum of the indices of all of the cards containing that number, i.e. all of its digits using the given sequence.
s = 0
for c in cards:
	displayCard(c)
	print
	if raw_input('Is your number on this card [y/n]? ') == 'y':
		s += c[0]

print 'Your number was', s

