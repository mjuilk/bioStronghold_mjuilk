def fin(file):
    try:
        f = open(file, 'r')
        for line in f:
            nr = line.split()
            nr = list(map(int, nr))
            return nr
    except:
        print('No such file exists')

def fib(pin):
    ls = fin(pin)
    #First number is total months
    #Second number is lifespan of rabbits
    ages = [1] + [0] * (ls[1] - 1)
    for i in range(ls[0] - 1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)

print(fib("rosalind_fibd.txt"))