#a
a= int(input("nhap mot so nguyen duong a="))
tong=0
while a>0:
    tong= tong + a%10;
    a= a//10;
print("tong cac chu so la", tong)
#b
n= int(input("nhap so nguyen duong n="))
tong=0
for i in range(1,n+1):
    if n%i==0:
        tong=tong+i
print("tong cac uoc cua n la",tong)
#c
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))
if a+b>c and a+c>b and b+c>a:
    if a*a==b*b+c*c or a*a+b*b==c*c or a*a+c*c==b*b:
        print("abc la tam giac vuong")
    elif a==b and b==c:
        print("abc la tam giac deu")
    elif a==b or b==c or b==c:
        print("abc la tam giac can")
    elif a*a>b*b+c*c or a*a+b*b<c*c or a*a+c*c<b*b:
        print("abc la tam giac tu")
    else:
        print("abc la tam giac nhon")
else:
    print("abc khong phai tam giac")
