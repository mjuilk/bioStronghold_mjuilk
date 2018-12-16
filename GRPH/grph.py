def fin(file):
    try:
        with open(file, 'r') as f:
            f = [x.strip() for x in f.readlines()]
            return f
    except Exception as e:
        print('No such file \n', e)
        
def dicCreate(f):
    fasta = {}
    counter = 0
    for line in f:
        if line.startswith('>'):
            fasta[line] = f[counter + 1]
            counter += 2
        else:
            pass
    return fasta

def graphCreate(dic, k):
    try:
        k += 1
    except TypeError:
        print("k must be an integer")
    fullGraph = []
    

def main():
    pin = fin("sample.txt")
    dic = dicCreate(pin)
    return graphCreate(dic, 3)

print(main())