# Some people have a problem understanding the mathematical arguments for the
# solution to the Monty Hall Problem, so here's an empirical argument.
#
# This program simulates a number of runs of the Monty Hall problem and compares
# two strategies: always switching doors and never switching.

from random import randint, choice
from optparse import OptionParser

# Generate three doors, one hiding a car (True) and two hiding goats (False)
# Also returns the location of the car as the second element in the tuple
def generate_doors():
    doors = [False, False, False]
    car_index = randint(0,2)
    doors[car_index] = True
    return (doors, car_index)


# Run a game and return the outcome as a 2-tuple of the form (always, never)
# Where True means the strategy won and False means it lost - e.g. (True, False)
# means the always switch strategy won and the never switch strategy lost
def simulate_game():
    available_doors = [0, 1, 2]
    (doors, car_index) = generate_doors()
    choice = randint(0,2)
    available_doors.remove(choice)

    # If the player never changes doors, we can see if they won right now
    never_result = doors[choice]

    # Choose a door to open -- can't choose the door with the car or the door
    # the player chose
    host_choice = car_index
    while host_choice == car_index or host_choice == choice:
        host_choice = randint(0,2)
    available_doors.remove(host_choice)

    # What's behind the other door?
    always_result = doors[available_doors[0]]

    return (always_result, never_result)


# Run a series of games and print the outcome
def main():
    parser = OptionParser()
    parser.add_option('-n', '--num-simulations', help='The number of simulations to run', default=1000, type='int')
    (options, args) = parser.parse_args()

    always_sum = 0
    never_sum = 0
    game_count = options.num_simulations
    for i in range(0, game_count):
        always, never = simulate_game()
        if always:
            always_sum += 1
        if never:
            never_sum += 1
    print("After {} games:\nAlways: {:02.01f}% / Never {:02.01f}%".format(game_count, always_sum*100/game_count, never_sum*100/game_count))

if __name__ == '__main__':
    main()
