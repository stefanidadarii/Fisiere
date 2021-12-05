with open('c:/Users/User/Desktop/ListaClasei11A.txt', 'r') as f:
    elevi=list(f)
n=media=0
print('Nume','Prenume','Nota',sep='\t')
for i in elevi:
    elev=i.split()
    nota=int(elev[2])
    n,media=n+1,media+nota
    print(elev[0],elev[1],nota,sep='\t')
print('Media celor', n, 'elevi este', sum(media)/float(n))