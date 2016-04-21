def hamming(seq1, seq2):

"""
Determines the Hamming Distance between two given DNA sequences.
"""

    diff_count = 0

    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            diff_count += 1

    return diff_count
