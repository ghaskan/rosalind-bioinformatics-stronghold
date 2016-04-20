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

def calculate_cg(sequence):
    """Calculate the CG content of a sequence as a percentage."""

    cg = 0

    for base in sequence:
        if base == 'C' or base == 'G':
            cg += 1

    return cg_content = (cg / len(sequence)) * 100

def max_cg(filepath):
    """Determines which FASTA format sequence from a text file collection has the highest CG content."""

    fasta = parse_fasta(filepath)
    max_label = ''
    max_cg = 0

    for label, sequence in fasta.items():
        cg = calculate_cg(sequence)   
        if cg > max_cg:
            max_cg = cg
            max_label = label

    return '{0}{1}{2}'.format(max_label, '\n', max_cg)
