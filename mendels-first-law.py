def mendel(k,m,n):

    total = k+m+n

    # calculating recessive offspring
    # recessive x recessive
    rec_rec = (n / total) * ((n-1) / (total-1))
    print(rec_rec)
    # het x het
    het_het = ((m / total) * ((m-1) / (total-1))) * (1/4)
    print(het_het)
    # het x recessive
    het_rec = (((m / total) * (n / (total - 1))) + ((n / total) * (m / (total-1)))) * (1/2)
    print(het_rec)

    return (1-rec_rec-het_het-het_rec)
