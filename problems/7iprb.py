# 7 IPRB Mendel's First Law

# k = AA
# m = Aa
# n = aa

# pr(k*k) = (k/pop)((k-1)/(pop-1)) -> 1
# pr(k*m) = (k/pop)(m/(pop-1)) -> 0.5 + 0.5 = 1 => (2)
# pr(k*n) = (k/pop)(n/(pop-1)) -> 1 => (2)
# pr(m*m) = (m/pop)((m-1)/(pop-1)) -> 0.25 + 0.5 = 0.75
# pr(m*n) = (m/pop)(n/(pop-1)) -> 0.5 => (1)

# what is the probability that any two random mates will produce an offspring with at least one dominant allele?
# kk, km, kn, mm, mn OR mk, nk, nm
def Mendel(k,m,n):
    pop = k + m + n
    probability = ((k**2)-k+(2*k*m)+(2*k*n)+(0.75*(m**2))-(0.75*m)+(m*n))/(pop*(pop-1))
    return probability

k = 15
m = 23
n = 22
print(Mendel(k,m,n))