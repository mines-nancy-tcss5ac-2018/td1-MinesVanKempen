f = open('names.txt', 'r')

def solve():
    for x in f:
        noms=x[1:len(x)-1].split('","')
        nomstries=sorted(noms)
        s=0
        for i in range (len(noms)):
            a=0
            for x in nomstries[i]:
                a+=ord(x)-64 #pour respecter la valeur des lettres donnees par le sujet
            s+=a*(i+1)
    return s

print(solve())
