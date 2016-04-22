def find_motif(s,t):
  
  # here we check each 0-index to find the motif starting at that position, but we only want to find the first instance,
  # so we only accept the result if it is equal to the index we're starting at, e.g. , if we start at pos 3 and find a hit
  # on pos 4, we pass on it, but if we start at pos 6 and find a hit at that position, we store that index in our list.
  # We add +1 to the results to comply with Rosalind's request 1-index results.
  pos_list = [i+1 for i in range(len(s)) if s.find(t, i) == i]

  return ' '.join(list(map(str,pos_list))) # formatting
