a,b,c=int(input()),int(input()),int(input())
D=b**2-4*a*c
if D<0:
    print("нет действительных корней")
else:
    x1=((-b)+D**0.5)/(2*a)
    x2=((-b)-D**0.5)/(2*a)
    if x1==x2:
        print(x1)
    else:
        print(x1,x2)