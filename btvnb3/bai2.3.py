k=int(input("ma tran a co so phan tu la: "))
a=[int(input(f"a[{i}]="))for i in range(k)]
n=int(input("so dong cua ma tran la: "))
m=int(input("so cot cua ma tran la: "))
X=[]
if n*m>k:
    print("no")
else:
    for i in range(n):
        a1 = a[i * m : (i + 1) * m]
        X.append(a1)
    print(X)
        