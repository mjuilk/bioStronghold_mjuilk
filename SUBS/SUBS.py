#Rosalind | Finding a Motif in DNA

def findMotif(DNA, repeat):
    pos_LS = list()
    counter = 0
    while True:
        if counter == len(DNA) - len(repeat):
            if DNA[counter:] == repeat:
                pos_LS.append(counter + 1)
            break
        elif DNA[counter:counter + len(repeat)] == repeat:
            pos_LS.append(counter + 1)
        counter += 1
    final = ""
    for i in pos_LS:
        final = final + str(i) + " "
    return final
            
with open("rosalind_subs.txt", 'r') as f:
    file = [x.strip() for x in f.readlines()]
    print (findMotif(file[0], file[1]))