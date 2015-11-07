# Guess a number chosen by the user using a clever trick
import math


# Generate a stack of cards given the indices of the cards and the largest number to be represented
def generateCards(indices, limit):
    ncards = len(indices)
    indices = sorted(indices)[::-1]
    # The highest number representable with the list is 1111 ... 111, which is the sum of all elements
    if limit > sum(indices):
        print "Cannot generate enough cards using the given indices."
        return []
    cards = []
    # Initialize each card to be an empty list
    for i in range(0, ncards):
        cards.append([])
    # Iterate over the numbers from 1 to limit (inclusive) and
    # figure out their representations in the given number system
    for n in range(1, limit+1):
        # Figure out which cards need to have n on them
        appearsOn = []
        nt = n
        # Go through the positions in reverse order subtracting out
        # the largest one that fits each time. This gives us the number's
        # representation in the given number system and therefore tells
        # us which cards need to have n on them
        for i in range(0, ncards):
            if nt >= indices[i]:
                nt -= indices[i]
                appearsOn.append(i)
        # Add n to the correct cards
        for c in appearsOn:
            cards[c].append(n)
    return cards


# Display a card in a pleasing way
def displayCard(card):
    nitems = len(card)
    displaysize = int(math.sqrt(nitems))+1

    # Make the top edge of the frame
    print '+' + '='*((displaysize*3)+1) + '+'
    for i in range(0, displaysize):
        # Left frame edge
        print '|',
        for j in range(0, displaysize):
            index = j+i*displaysize
            # Display the next number
            if index < nitems:
                print "%2i" % card[index],
            # Past the end of the array, print blank spaces
            else:
                print '  ',
        # Right frame edge
        print '|'
    # Bottom frame edge
    print '+' + '='*((displaysize*3)+1) + '+'


# Generate cards using the first few Fibonacci numbers and a max value of 30
maxGuess = 50
cards = generateCards([1, 2, 3, 5, 8, 13, 21], maxGuess)

print 'Think of a number between 1 and %i.'
s = raw_input('Press enter when you\'ve decided on a number.')
print ''
print 'Now I\'ll show you some cards and you just have to tell me if you see your number.'
print ''


# The player's number is just the sum of the indices of all of the cards
# containing that number, i.e. all of its digits using the given sequence.
s = 0
for c in cards:
    displayCard(c)
    print
    if raw_input('Is your number on this card [y/n]? ') == 'y':
        s += c[0]

print 'Your number was', s
