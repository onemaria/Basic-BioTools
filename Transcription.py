DNA_Nucleotides = ['A', 'C', 'G', 'T']
DNA_Transcription = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}

def transcribe(seq):
    seq = seq.upper()
    transcription=""
    for nucleotides in seq:
        if nucleotides not in DNA_Nucleotides:
            return "The sequence contains a non nucleotide. Please check and insert again a correct sequence"
    for pos in seq:
        for key, value in DNA_Transcription.items():
            if key == pos:
                transcription += value
    return transcription
    