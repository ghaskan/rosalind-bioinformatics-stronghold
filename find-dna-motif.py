def find_motif(s,t):
    
    # create a list with the 0-indexes where the motif is found in the sequence
    hits = [s.find(t,i) for i in range(len(s))]
    
    # clean the list by elimating 
    hits = list(filter(lambda x: x > -1, hits)) # filters negative results while keeping a list
    hits = sorted(set(hits)) # set removes duplicates, sorted turns the objected into a sorted list
    hits = map(lambda y: y+1, hits) # transforming our 0-index results into Rosalind's desired 1-index results

    return ' '.join(list(map(str,hits))) # transforming our list into a string with the desired formatting
