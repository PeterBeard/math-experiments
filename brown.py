"""
Guess a number chosen by the user using a clever trick

Based on this Numberphile video:
https://www.youtube.com/watch?v=kQZmZRE0cQY
"""
import math


def generateCards(indices, limit):
    """Generate a stack of cards given the indices and the largest number"""
    ncards = len(indices)
    indices = sorted(indices)[::-1]
    # The highest number representable with the list is 1111 ... 111, which is the sum of all elements
    if limit > sum(indices):
        print("Cannot generate enough cards using the given indices.")
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


def display_card(card):
    """Display a card in a pleasing way"""
    nitems = len(card)
    char_width = 6
    display_size = int(math.sqrt(nitems))+1
    fill_width = (display_size * char_width) + 1

    # Make the top edge of the frame
    print('\u2554' + '\u2550'*fill_width + '\u2557')
    for i in range(0, display_size):
        # Empty row
        print('\u2551' + ' '*fill_width + '\u2551')
        # Left frame edge
        print('\u2551', end='')
        for j in range(0, display_size):
            index = j+i*display_size
            # Display the next number
            if index < nitems:
                print("{: ^6n}".format(card[index]), end='')
            # Past the end of the array, print blank spaces
            else:
                print(' '*char_width, end='')
        # Right frame edge
        print(' \u2551')

    # Bottom frame edge
    print('\u255a' + '\u2550'*fill_width + '\u255d')


# Generate cards using the first few Fibonacci numbers and a max value of 30
MAX_GUESS = 50
cards = generateCards([1, 2, 3, 5, 8, 13, 21], MAX_GUESS)

print('Think of a number between 1 and {0}.'.format(MAX_GUESS))
s = input('Press enter when you\'ve decided on a number.\n')
print('Now I\'ll show you some cards and you just have to tell me \
        if you see your number.\n')


# The player's number is just the sum of the indices of all of the cards
# containing that number, i.e. all of its digits using the given sequence.
s = 0
for c in cards:
    display_card(c)
    if input('\nIs your number on this card [y/n]? ').lower() == 'y':
        s += c[0]

print('\n\n{:^80}\n\n'.format('Your number was {}.'.format(s)))
