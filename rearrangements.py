import itertools

def rearrange(filepath):

    """
    A permutation of length n is an ordering of the positive integers from 1 till n.
    Given: A positive integer n.
    Return: The total number of permutations of length n, followed by a list of all such permutations.
    """

    with open(filepath, 'r') as f:
        # obtaining our n
        n = f.read().rstrip('\n').rstrip('\r')
        n = int(n)

        # creates a list of length n, then create a list of possible permutations of n length, each represented
        # as a tuple.
        to_permute = list(range(1, n+1))
        permutations = list(itertools.permutations(to_permute, n))

        with open('C:\\Users\\Marta\\Desktop\\derp.txt', 'w') as out:
            # writing in the output how many permutations we found
            out.write(str(len(permutations)) + '\n')

            # adding our permutations in the requested format
            for item in permutations:
                out.write(' '.join(map(str, item)) + '\n')

    return "All done!"
