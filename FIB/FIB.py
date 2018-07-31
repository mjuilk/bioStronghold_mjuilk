#Rosalind | Rabbits and Recurrence Relation

'''f = open("rosalind_fib.txt", "r")  #File opening bullshit
data = f.read()                       #Site gives .txt file as data
ls = [int(x) for x in data.split()]   #So I just did this
n,k = ls[0], ls[1]'''

n = 29
k = 4

def rabbit(months, offspring):
    final = 0
    a = 1 
    b = 1 
    c = 1
    if months == 1 or months == 2:
        final = 1
    else:
        counter = 2
        while True:
            c = b * offspring
            final = a + c
            counter += 1
            if counter == months:
                break
            else:
                b = a
                a = final
                
    return final
        

print (rabbit(n, k))
f.close()