#Rosalind | Computing GC Content

def GC(DNA):
    dict = {
            'A' : 0,
            'T' : 0,
            'G' : 0,
            'C' : 0
            }
    dict['A'] = DNA.count('A')
    dict['T'] = DNA.count('T')
    dict['C'] = DNA.count('C')
    dict['G'] = DNA.count('G')
    CONTENT = ((dict['C'] + dict['G'])/len(DNA))
    return CONTENT

file = open("rosalind_gc.txt", "r")
f = file.read().split('\n')
ID_LS = [x for x in f if x.startswith('>') == True]
ID_INDEX_LS = [f.index(x) for x in f if x.startswith('>') == True]

DNA_LS = list()
counter = 0
while True:
    try:
        DNA_INDEX_LS = [x for x in range((ID_INDEX_LS[counter] + 1),
                                         ID_INDEX_LS[counter + 1])]
        DNA_TEMP = list()
        for x in DNA_INDEX_LS:
            DNA_TEMP.append(f[x])
        DNA_TEMP = "".join(DNA_TEMP)
        DNA_LS.append(DNA_TEMP)
        counter += 1
        if counter == len(ID_INDEX_LS):
            break
    except IndexError:
        DNA_INDEX_LS = [x for x in range((ID_INDEX_LS[-1] + 1), len(f))]
        DNA_TEMP = list()
        for x in DNA_INDEX_LS:
            DNA_TEMP.append(f[x])
        DNA_TEMP = "".join(DNA_TEMP)
        DNA_LS.append(DNA_TEMP)
        break

GC_LS = [GC(x) for x in DNA_LS]
HIGH_INDEX = GC_LS.index(max(GC_LS))
print(ID_LS[HIGH_INDEX])
print(GC_LS[HIGH_INDEX] * 100, '\n')