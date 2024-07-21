#a
n=int(input("n="))
print("S(n)=",n+1)
#b
n=int(input("n="))
S=0
for i in range(1,n+1):
    if n==0:
        print("khong tinh duoc S(n)")
    if n>0:
        S=float(S+1/i)
print("S(n)",S)
#c
a= float(input("he so bac 2 la "))
b= float(input("he so bac 1 la "))
c= float(input("he so bac 0 la "))
delta= b*b- 4*a*c
if delta<0:
    print("phuong trinh vo nghiem")
elif delta==0:
    print("phuong trinh co nghiem kep x1=x2=", -b/(2*a))
else:
    x1=(-b + delta**(1/2))/(2*a)
    x2=(-b - delta**(1/2))/(2*a)
    print("phuong trinh co 2 nghiem phan biet")
    print("x1=",x1)
    print("x2=",x2)
    