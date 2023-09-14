# 3 REVC Complementing a Strand of DNA

# from the Hidden Messages project
def ReverseComplement(Text):
    Text = Reverse(Text)
    Text = Complement(Text)
    return Text

def Reverse(Text):
    rev = ""
    for char in Text:
        rev = char + rev
    return rev

def Complement(Text):
    comp = ""
    basepairs = {"A":"T", "T":"A", "C":"G", "G":"C"}
    for char in Text:
        comp = comp + basepairs.get(char)
    return comp

Text = "TTACGTGGAGGTCTAACCGCATCGTCGGGCCGAATCGGCCATTGCTTGGACTCCGGATGGAGCCGGCACGGTCAGGCTTATCCAGAATTATGCGTTCGGTATGCAATACTCAACCCAGCGACTTCATGTTCCTTAGTCCATCTCTCGAACGTGGGACATGAATATAGATTGTCGTTTTAAAGGAGTACTTAGGATAAAGATTGAGCTCCTCGAAGGGACACCGGCTCTACTGAGCACTAACTAGTCTCTGCGGCTGATCTACTCAGTCGGTTTTCCCTCCGCGTTAACTTAATTCAATGATACGGCCCCTTTATGCGATACCACGCGCGCTACGTATGAGCAGCGCGCGGAAGTGTCTGATATGTGCTCTGCCCGTCGCCCGGAACGTGGGCCCTGTTACTTAAGAAATACCACGGACGCCCGGGAAGGAATCACGCCCAGCGTGATACTCACCAGACCTGTCGTTCATGGACTTTACTACAACGGTCTGTATACTTCCTAAGTCCAGACAACTTCGGAACCTAGTCCGAGAGTAGAATGGCAGCCCGGACGTACATCAGTGGTTATTTGCTCATCGTATGTGCATATGAAACCCGTATTCGGTGATGAAGTACGGAGCTCTTCATTGGGTCGCGGGGAGTGAGTGTGCAACACGCCAGATAATAGTTGACATCACAATAATACTGCGTGTTTCGCAGCGACGAGTTCCAACTGTTACCGTAGACTATTGGACGAGATTCGCCCACCAGCAAAATCTGGGGCAGTGCAGAACCATAGAGCCTTAAGTGTGGAGGTTCTCTCTGCTATGTTATATGTGCCGGATGTTTAGCTAGATGGGGAATTAGGGCCGATCAACTAGCCTAACATGTAGA"
print(ReverseComplement(Text))

# SIMPLER SOLUTION
def ReverseComplement(Text):
    Text = Text.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    return Text