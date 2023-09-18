# 5 GC Computing GC Content

# import module to read FASTA files
from Bio import SeqIO

highest = 0
# convert file location to a raw string
handle = open(r"example.fasta")
for record in SeqIO.parse(handle, "fasta"):
    count = 0
    total = 0
    for i in record.seq:
        total +=1
        if i == "G" or i == "C":
            count +=1
    percent = count/total*100
    # to save the highest-scoring record
    if percent > highest:
        highest = percent
        ID = record.id

print(ID)
print(highest)
handle.close()
