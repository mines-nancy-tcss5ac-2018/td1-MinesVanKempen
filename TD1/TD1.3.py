def estPalyndrome(n):
    a=str(n)
    l=len(a)//2
    for i in range(l):
        if a[i]!=a[-i-1]:
            return False
    return True

assert estPalyndrome(3)==True
assert estPalyndrome(313)==True
assert estPalyndrome(3131)==False

def reverseAndAdd(n):
    a=''
    txt=str(n)
    for i in range(len(txt)):
        a+=(txt[-i-1])
    return (n+int(a))

assert reverseAndAdd(349)==1292
assert reverseAndAdd(4213)==7337

def estLychrel(n,t=50):
    n=reverseAndAdd(n)
    for i in range(t):
        if estPalyndrome(n):
            return True
        n=reverseAndAdd(n)
    return False
        
assert estLychrel(349)
assert estLychrel(196)==False
assert estLychrel(10677)==False
assert estLychrel(10677,54)

def solve(n):
    s=0
    for i in range(n):
        if estLychrel(i)==False:
            s+=1
    return s

print(solve(10000))