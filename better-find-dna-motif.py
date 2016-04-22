def find_motif(s,t):

  pos_list = [i for i in range(len(s)) if s.find(t, i) == i]

  return ' '.join(list(map(str,pos_list)))
