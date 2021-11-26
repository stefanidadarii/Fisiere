with open ('c:/Users/User/Desktop/input.txt', 'r') as f:
    V=f.readline()
nr_vocale=0
vocale='aeiouAEIOU'
with open('c:/Users/User/Desktop/output.txt', 'w') as f:
    for i in V:
        if i in vocale:
            f.write("Vocalele sunt:"+i)
            nr_vocale+=1
print('Numarul vocalelor este:', numar_vocale)
