input_file = open('', 'r') # input location
output_file = open('','w') # output location

dna_string = input_file.read()
rna_string = ''

for nt in dna_string:
    # remove newlines
    nt = nt.rstrip('\n')
    nt = nt.rstrip('\r')
    # ignore blank results
    if nt == '':
        continue
    nt = nt.replace('T', 'U')
    rna_string += nt

output_file.write(rna_string)

input_file.close()
output_file.close()
