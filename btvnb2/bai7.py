def uoc(n):
    sum=0
    for i in range(1, n//2+1):
        if n%i==0:
            sum =sum+ i
    return sum
n= int(input("n= "))
for i in range(1, n+1):
    sum=uoc(i)
    if uoc(sum)==i and sum<i:
        print(i);