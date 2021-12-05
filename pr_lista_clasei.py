with open('c:/Users/User/Desktop/Lista Clasei 11A.txt', 'r') as f:
    elevi=list(f)
n=media=0
print('Nume','Prenume','Nota','Limba',sep='\t')
a=open('c:/Users/User/Desktop/Elevii_Ce_Studiaza_LimbaEngleza.txt', 'w', encoding='utf-8')
b=open('c:/Users/User/Desktop/Elevii_Ce_Studiaza_LimbaGermana.txt', 'w', encoding='utf-8')
for i in elevi:
    elev = i.split()
    nota=int(elev[2])
    n,media=n+1,media+nota
    print(elev[0],elev[1],nota,elev[3], sep='\t')
    if elev[3].lower() == 'engleza':
        a.write(elev[0]+elev[1]+str(nota)+'\n')
    elif elev[3].lower() == 'germana':
        b.write(elev[0]+elev[1]+str(nota)+'\n')
print('Media celor', n, 'elevi este', media/float(n))
a.close()
b.close()
