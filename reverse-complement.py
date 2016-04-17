input_file = open('', 'r') # input location
output_file = open('', 'w') # output location

dna_string = input_file.read()
dna_complement = ''

for nt in dna_string:
    # remove newlines
    nt = nt.rstrip('\n')
    nt = nt.rstrip('\r')
    # ignore blank results
    if nt == '':
        continue
    # check which nt we're dealing with
    if nt == 'A':
        nt = nt.replace('A', 'T')
    elif nt == 'T':
        nt = nt.replace('T', 'A')
    elif nt == 'G':
        nt = nt.replace('G', 'C')
    elif nt == 'C':
        nt = nt.replace('C', 'G')
    # add obtained complement nt
    dna_complement += nt

reverse_complement = dna_complement[::-1] # reverse by using extended slice

output_file.write(reverse_complement)

input_file.close()
output_file.close()
