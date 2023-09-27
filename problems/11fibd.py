# 11 FIBD Mortal Fibonacci Rabbits

def MortalFibonacci(n, m):
    # following generations. 1 pair, 1 pair,...
    bunnies = [1,1]
    for i in range(n-2):
        # starting a new count, hence 0 and not 2
        count = 0
        # no deaths yet
        if i + 2 < m:
            count = bunnies[i] + bunnies[i+1]
        # accounting for death
        else:
            for j in range(m-1):
                count += bunnies[i-j]
        bunnies.append(count)
    return bunnies

n = 85
m = 17
print(MortalFibonacci(n, m))

# ALTERNATIVE SOLUTION - APPLYING FIB EQUATIONS
# generations = [1, 1] #Seed the sequence with the 1 pair, then in their reproductive month.
# def fib(i, j):
#     count = 2
#     while (count < i):
#         if (count < j):
#             generations.append(generations[-2] + generations[-1]) #recurrence relation before rabbits start dying (simply fib seq Fn = Fn-2 + Fn-1)
#         elif (count == j or count == j+1):
#             print ("in base cases for newborns (1st+2nd gen. deaths)") #Base cases for subtracting rabbit deaths (1 death in first 2 death gens)
#             generations.append((generations[-2] + generations[-1]) - 1)#Fn = Fn-2 + Fn-1 - 1
#         else:
#             generations.append((generations[-2] + generations[-1]) - (generations[-(j+1)])) #Our recurrence relation here is Fn-2 + Fn-1 - Fn-(j+1)
#         count += 1
#     return (generations[-1])