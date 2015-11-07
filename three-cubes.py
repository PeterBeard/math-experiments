# Find ways to express numbers as a sum of three integers cubed


# Find a solution (a, b, and c) to a^3 + b^3 + c^3 = n
# n is any integer
# max_n is the largest value of a, b, or c to check. Default is 250
def find_cubes(n, max_n=250):
    # Values of the form 9k+4 or 9k+5 are not expressible as the sum of three cubes
    if (n-4) % 9 == 0 or (n-5) % 9 == 0:
        return None
    # Limit ourselves to a fairly small search space
    for i in range(0, max_n):
        i_cubed = i**3
        for j in range(0, max_n):
            j_cubed = j**3
            for k in range(0, max_n):
                k_cubed = k**3

                # If this triple works,  return it
                if i_cubed + j_cubed + k_cubed == n:
                    return (i, j, k)
                elif i_cubed + j_cubed - k_cubed == n:
                    return (i, j, -k)
                elif i_cubed - j_cubed + k_cubed == n:
                    return (i, -j, k)
                elif -i_cubed + j_cubed + k_cubed == n:
                    return (-i, j, k)
                elif i_cubed - j_cubed - k_cubed == n:
                    return (i, -j, -k)
                elif -i_cubed - j_cubed + k_cubed == n:
                    return (-i, -j, k)
                elif -i_cubed + j_cubed - k_cubed == n:
                    return(-i, j, -k)
                elif -i_cubed - j_cubed - k_cubed == n:
                    return(-i, -j, -k)

    # We didn't find a solution :(
    return None


# Print an equation in a nice way
# n is the solution to the equation
# values is a 3-tuple of the form (a,b,c)
def print_sum(n, values):
    print ('%i = (%i)' + unichr(179) + ' + (%i)' + unichr(179) + ' + (%i)' + unichr(179)) %\
          (n, values[0], values[1], values[2])

# Get the values to check around
max_search = int(raw_input('How high shall I look for solutions? '))

for i in range(1, max_search+1):
    cubes = find_cubes(i)
    if cubes:
        print_sum(i, cubes)
    else:
        print '%i is not expressible as the sum of three integer cubes.' % i
