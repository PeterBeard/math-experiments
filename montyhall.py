# Some people have a problem understanding the mathematical arguments for the
# solution to the Monty Hall Problem, so here's an empirical argument.
#
# This program simulates a number of runs of the Monty Hall problem and compares
# two strategies: always switching doors and never switching.
from random import randrange, choice
from optparse import OptionParser


def pretty_print_game(doors, car_index, always_choice, never_choice):
    """
    Produce some pretty output for a given game
    """
    always_str = 'Always: Door #{}'.format(always_choice + 1)
    never_str = 'Never: Door #{}'.format(never_choice + 1)

    always_result = doors[always_choice]
    never_result = doors[never_choice]

    print('{}┏{}┓'.format(' '*20, '━'*14))
    print('{lines}┨ Game Results ┠{lines}'.format(lines='─'*20))
    print('{always:>19} ┗{lines}┛ {never}'.format(
        always=always_str,
        lines='━'*14,
        never=never_str
    ))
    print()
    left_offset = 21
    door_contents = ['✖'] * len(doors)
    door_contents[car_index] = '⛟'
    print(' '*left_offset, end='')
    print('┏━━━┓' * len(doors))
    print(' '*left_offset, end='')
    for idx in range(len(doors)):
        print('┃ {} ┃'.format(door_contents[idx]), end='')
    print()
    print(' '*left_offset, end='')
    print('┗━━━┛' * len(doors), end='')
    print()
    print(' '*left_offset, end='')
    for idx in range(len(doors)):
        if idx in {never_choice, always_choice}:
            print('  ↑  ', end='')
        else:
            print('     ', end='')
    print()
    print(' '*left_offset, end='')
    for idx in range(len(doors)):
        if idx == never_choice:
            print('  N  ', end='')
        elif idx == always_choice:
            print('  A  ', end='')
        else:
            print('     ', end='')
    print()
    if always_result:
        print('Always switch wins')
    elif never_result:
        print('Never switch wins')
    print()


# Generate three doors, one hiding a car (True) and two hiding goats (False)
# Also returns the location of the car as the second element in the tuple
def generate_doors():
    doors = [False, False, False]
    car_index = randrange(len(doors))
    doors[car_index] = True
    return (doors, car_index)


# Run a game and return the outcome as a 2-tuple of the form (always, never)
# Where True means the strategy won and False means it lost - e.g. (True, False)
# means the always switch strategy won and the never switch strategy lost
def simulate_game(verbose=False):
    available_doors = [0, 1, 2]
    (doors, car_index) = generate_doors()
    never_choice = randrange(len(doors))
    available_doors.remove(never_choice)

    # If the player never changes doors, we can see if they won right now
    never_result = doors[never_choice]

    # Next, the host will open a door the player didn't choose and that
    # doesn't have the car behind it
    host_choice = car_index
    while host_choice == car_index or host_choice == never_choice:
        host_choice = randrange(len(doors))
    available_doors.remove(host_choice)

    # What's behind the other door?
    always_choice = available_doors[0]
    always_result = doors[always_choice]

    # Pretty output if requested
    if verbose:
        pretty_print_game(doors, car_index, always_choice, never_choice)

    return (always_result, never_result)


# Run a series of games and print the outcome
def main():
    parser = OptionParser()
    parser.add_option('-n', '--num-simulations', help='The number of simulations to run', default=1000, type='int')
    parser.add_option('-v', '--verbose', help='Show the doors for every game',
            action='store_true', default=False)
    (options, args) = parser.parse_args()

    always_sum = 0
    never_sum = 0
    game_count = options.num_simulations
    verbose = options.verbose
    for i in range(0, game_count):
        always, never = simulate_game(verbose)
        if always:
            always_sum += 1
        if never:
            never_sum += 1
    print("After {} games:\nAlways: {:02.02f}% / Never {:02.02f}%".format(
        game_count,
        always_sum*100.0/game_count,
        never_sum*100.0/game_count)
    )

if __name__ == '__main__':
    main()
