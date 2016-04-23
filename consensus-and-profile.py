# auxiliary functions

def parse_fasta(filepath):

    """Parse the contents of a file containing a FASTA file and returns them in dictionary form."""

    # setting up our storage variables
    fasta = {}
    current_seq = ''

    # let's open our file and read each line as the item of a list
    with open(filepath, 'r') as f:
        data = f.readlines()

        # iterating the list
        for item in data:
            # if the first character in our list item is a >, that means we've hit a label
            if item[0] == '>':

                # we try to assign a sequence to our current label, but since we're starting there's no sequence yet
                try:
                    # add our current sequence as our current key's value before moving onto the next ones.
                    fasta[current_key] = current_seq

                except UnboundLocalError:
                    pass

                # but, no matter what, we want to assign our labels to a variable (while stripping away all of its
                # goodies) and we want to reset our current sequence variable to ready it to read the next one
                current_key = item.lstrip('>').rstrip('\n').rstrip('\r')
                current_seq = ""

            # when we aren't dealing with a label...
            else:
                # we want to keep constructing our current sequence!
                current_seq += item.rstrip('\n').rstrip('\r')

        # since we won't add any more labels, we want to assign our last current key and sequence pair to our dictionary
        fasta[current_key] = current_seq

        return fasta

def list_sequences(filepath):
    """
    Opens a given filepath pointing to a file containing sequences in FASTA format, and transforms them into a
    plain list.
    """

    with open(filepath, 'r') as f:

        # let our previous function do the parsing work
        fasta_list = parse_fasta(filepath)
        # create a list where each sequence is an item
        seq_list = [fasta_list[key] for key in fasta_list.keys()]

    return seq_list

def compare_sequences(filepath):
    """
    We'll compare various sequences in the FASTA format by creating a dictionary denoting the number of times a given
    base happens in a certain position in all sequences (e.g., if we compare "ATC" and "TCA", our line for A would be
    'A': [1, 0, 1])
    """

    seq_list = list_sequences(filepath) # use our previous function to create a list of sequences

    base_count = {'A' : [0] * len(seq_list[0]), 'C' : [0] * len(seq_list[0]), 'G' : [0] * len(seq_list[0]),
            'T': [0] * len(seq_list[0])} # create a base 'matrix' dictionary

    # using these two for loops we'll navigate our list's items per column, i.e., we'll check index i in all items
    # before moving to the next index.
    for i in range(len(seq_list[0])):
        for item in seq_list:

            # if the character in index i for our item is the base adenine, we add +1 to the equivalent position in the
            # dictionary 'matrix'.
            if item[i] == 'A':
                base_count['A'][i] += 1

            # second verse same as the first, and so forth.
            elif item[i] == 'C':
                base_count['C'][i] += 1

            elif item[i] == 'G':
                base_count['G'][i] += 1

            elif item[i] == 'T':
                base_count['T'][i] += 1

    return base_count

def find_consensus(filepath):
    """
    We build a profile matrix using the compare_sequences function, then iterate over each column of the matrix and
    check the first maximum value, which will decide the base to be added to our consensus sequence.
    """

    profile_matrix = compare_sequences(filepath)
    consensus_seq = [] # list where each base of the sequence will be saved

    # using two for loops we'll navigate our matrix's items per column, i.e., we'll check index i in all items
    # before moving to the next index.
    for i in range(len(profile_matrix['A'])):

        # here we try to append the key that matches the first maximum value of the i-1th column.
        # if that fails, this block of code will be ignored and we'll look for our first first maximum (depicted here is
        # the result of poor choice of wording).
        try:
            consensus_seq.append(current_key)

        except UnboundLocalError:
            pass

        # we define our first maximum as a value that will be surpassed no matter what by the values in our profile
        # matrix, and we define the current key that will be deleted after the value from the previous iteration has
        # been stored in the consensus_seq list.
        max = -1
        current_key = ''

        # navigating the column and finding our first maximum and its respective base (key).
        for key, value in profile_matrix.items():
            if value[i] > max:
                max = value[i]
                current_key = key

    # appending the key that matches the first maximum value in the last column.
    consensus_seq.append(current_key)

    return  ''.join(consensus_seq)

# main output function

def consensus(input_filepath, output_filepath):
    """
    Builds a prettier output to display the result of the work of all previous functions, and, most importantly, is the
    only function that needs to be called.
    """

    profile_matrix = compare_sequences(input_filepath)

    with open(output_filepath, 'w') as out:

        out.write(find_consensus(input_filepath) + '\n')
        out.write('A: ' + ' '.join(map(str,profile_matrix['A'])) + '\n')
        out.write('C: ' + ' '.join(map(str, profile_matrix['C'])) + '\n')
        out.write('G: ' + ' '.join(map(str, profile_matrix['G'])) + '\n')
        out.write('T: ' + ' '.join(map(str, profile_matrix['T'])) + '\n')

    return 'All done!'
