def solve(a,n):
    result = a**n
    digits=[]
    s=0
    for x in str(result):
        s+=int(x)
    return s

assert solve(2,15) == 26
print (solve (2,1000))
