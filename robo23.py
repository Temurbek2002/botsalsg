class arithmetic:
    def f(a,b,c):
        s=(a+b)/(2*a+c)+5*a/(2*b-c)
        d="%.3f"%s
        return(d)
r=arithmetic
x,y,z=map(int,input().split())
print(r.f(x,y,z))