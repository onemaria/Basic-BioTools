from Transcription import transcribe
from Translation import translate
from GCcontent import GCcont

seq = input("Insert DNA sequence to be analyzed: ")

print("The transcription of the sequence is: ", transcribe(seq))
print("The translation of the sequence is: ", translate(seq, 0))
print("The sequence has ", GCcont(seq))

#write the result in a file
f= open("aboutSEQ.txt","w+")
f.write("The DNA sequence analyzed is: " + seq + "\n")
f.write("\n The transcription of the sequence is: " + transcribe(seq))
f.write("\n The translation of the sequence is: " + translate(seq, 0))
f.write("\n The sequence is " + str(len(seq)) + " base pairs long.")
f.write("\n The sequence has a "+ GCcont(seq))
f.close()
