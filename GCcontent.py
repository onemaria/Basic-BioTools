DNA_Nucleotides = ['A', 'C', 'G', 'T']

def GCcont(seq):
    seq = seq.upper()
    GCcontent = 0
    for nucleotides in seq:
        if nucleotides not in DNA_Nucleotides:
            return "The sequence contains a non nucleotide. Please check and insert again a correct sequence"
    for pos in seq:
        if pos == 'G' or pos == 'C':
            GCcontent += 1
    return f"{GCcontent/len(seq)*100:.2f}" + " % GC content"
    