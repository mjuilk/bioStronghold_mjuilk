#Rosalind | Mendel's First Law

#file = open("IPRB.txt", "r")
file = open("iprb.txt", "r")
f = file.read().split()
ls = [float(x) for x in f]

PLS = [(x / sum(ls)) for x in ls]

dict = {
        'AA_AA': PLS[0] * ((ls[0]-1)/(sum(ls)-1)),   #1
        'AA_Aa': PLS[0] * (ls[1]/(sum(ls)-1)),   #2
        'AA_aa': PLS[0] * (ls[2]/(sum(ls)-1)),   #3
        'Aa_Aa': (PLS[1] * ((ls[1]-1)/(sum(ls)-1))) * 0.75,   #4
        'Aa_aa': (PLS[1] * (ls[2]/(sum(ls)-1))),   #5
        }
print('dict 1: ', dict, '\n')

final = round(dict['AA_AA'] + dict['AA_Aa'] * 2 + dict['AA_aa'] * 2 
+ dict['Aa_Aa'] + dict['Aa_aa'], 5)

print('final: ', final, '\n')

print('dict 2: ', dict, '\n')

weird_final = dict['AA_AA'] + dict['AA_Aa'] * 2 + dict['AA_aa'] * 2 
+ dict['Aa_Aa'] + dict['Aa_aa']

print('weird_final: ', weird_final, '\n')

print('dict 3: ', dict, '\n')

file.close()