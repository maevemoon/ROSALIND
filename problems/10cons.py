# 10 CONS Consensus and Profile

from Bio import SeqIO
import numpy 

# the Hidden Messages project contains a more concise approach for this challenge but i struggled to adapt it to fasta and numpy

sequences = []                             
handle = open(r"cons.fasta")     
for record in SeqIO.parse(handle, "fasta"):
    sequence = []                         
    for i in record.seq:                 
        sequence.extend(i)              
    sequences.append(sequence)            
handle.close() 

k = len(sequences[0])
# x * y zeros matrix; an empty base where counts will be filled in - appears as 0 0 0 0 ... where x = height, y = length
matrix = numpy.zeros((4,k), dtype = int)

# i and j search for positions, line and nt search for anything (the symbols, in this case)
for i,line in enumerate(sequences):
    for j,nt in enumerate(line):
        if nt == "A":
            matrix[0][j] +=1
        elif nt == "C":
            matrix[1][j] +=1
        elif nt == "G":
            matrix[2][j] +=1
        elif nt == "T":
            matrix[3][j] +=1

consensus = ""
# zip = groups lines, shortens code
for A,C,G,T in zip(matrix[0], matrix[1], matrix[2], matrix[3]):
    if A >= C and A >= G and A >= T:
        consensus += "A"
    elif C >= A and C >= G and C >= T:
        consensus += "C"
    elif G >= A and G >= C and G >= T:
        consensus += "G"
    elif T >= C and T >= G and T >= C:
        consensus += "T"

# formatting
print(consensus)
# str(i) turns the variable into a string to use
print("A: " + " ".join(str(i) for i in matrix[0]))
print("C: " + " ".join(str(i) for i in matrix[1]))
print("G: " + " ".join(str(i) for i in matrix[2]))
print("T: " + " ".join(str(i) for i in matrix[3]))

# matrix = numpy.array(sequences)