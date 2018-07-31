#Rosalind | Translating RNA into Protein

codon_dict = {
        'UUU' : 'F', 'UUC' : 'F',
        'UUA' : 'L', 'UUG' : 'L',
        'UCU' : 'S', 'UCA' : 'S', 'UCC' : 'S', 'UCG' : 'S',
        'UAU' : 'Y', 'UAC' : 'Y',
        'UAA' : '', 'UAG' : '',
        'UGU' : 'C', 'UGC' : 'C',
        'UGA' : '',
        'UGG' : 'W',
        'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L',
        'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
        'CAU' : 'H', 'CAC' : 'H',
        'CAA' : 'Q', 'CAG' : 'Q',
        'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R',
        'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I',
        'AUG' : 'M',
        'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T',
        'AAU' : 'N', 'AAC' : 'N',
        'AAA' : 'K', 'AAG' : 'K',
        'AGU' : 'S', 'AGC' : 'S',
        'AGA' : 'R', 'AGG' : 'R',
        'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V',
        'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
        'GAU' : 'D', 'GAC' : 'D',
        'GAA' : 'E', 'GAG' : 'E',
        'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G'
        }

with open('rosalind_prot.txt', 'r') as file:
    f = file.read()
    f = f.rstrip()
    a = f
    prot = ""
    
    counter = 0
    while True:
        codon = a[0:3]
        prot = prot + codon_dict[codon]
        a = a[3:]
        counter += 1
        if counter == (len(f)/3) - 1:
            break
    print (prot)