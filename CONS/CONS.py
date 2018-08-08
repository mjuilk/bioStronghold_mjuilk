with open("rosalind_cons.txt", "r") as file:    
    f = file.readlines()
    f = [x.rstrip() for x in f]
    rosls = []
    for i in f:
        if i.startswith(">") == True:
            rosls.append(f.index(i))
    counter = 0
    f_true = []
    while True:
        try:
            a = ''.join(f[rosls[counter] + 1:rosls[counter + 1]])
            f_true.append(a)
            counter += 1
        except IndexError:
            a = ''.join(f[rosls[counter] + 1:])
            f_true.append(a)
            break
##############################################################################
    A, C, G, T = [],[],[],[]
    f_true = [x.rstrip() for x in f_true]
###################################
    counter = 0
    #try:
    while True:
        if counter == len(f_true[0]):
            break
        ls = []
        for i in f_true:
            ls.append(i[counter])
        A.append(ls.count('A'))
        C.append(ls.count('C'))
        G.append(ls.count('G'))
        T.append(ls.count('T'))
        counter += 1
    #except IndexError:
                
###################################  
    cons = ""
###################################
    counter = 0
    NU = [A,C,G,T]
    while len(cons) != len(A):
        ls = []
        for i in NU:
            ls.append(i[counter])
        if max(ls) == A[counter]:
            cons += "A"
        elif max(ls) == C[counter]:
            cons += "C"
        elif max(ls) == G[counter]:
            cons += "G"
        elif max(ls) == T[counter]:
            cons += "T"
        counter += 1
##################################
    print (cons)
    print ("A:", *A)
    print ("C:", *C)
    print ("G:", *G)
    print ("T:", *T)