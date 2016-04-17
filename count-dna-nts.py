input = open('', 'r') # input location
output = open('','w') # output location

dna_string = input.read()
count = {}

for nucleotide in dna_string:
    # remove newlines
    nucleotide = nucleotide.rstrip('\n')
    nucleotide = nucleotide.rstrip('\r')
    # ignore blank results
    if nucleotide == '':
        continue
    # count the nt, update its value
    count[nucleotide] = count.get(nucleotide, 0) + 1

# we want our keys to be sorted alphabetically
# for the output we only want the values
for value in sorted(count):
    output.write(str(count[value]) + ' ')

input.close()
output.close()
