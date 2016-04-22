def find_motif(s,t):

    hits = [s.find(t,i) for i in range(len(s))]

    hits = list(filter(lambda x: x > -1, hits))
    hits = sorted(set(hits))
    hits = map(lambda y: y+1, hits)

    return ' '.join(list(map(str,hits)))
