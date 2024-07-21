def check(n):
    sum=0
    m=n
    while n>0:
        sum += (n%10)**3
        n=n//10
    return sum==m
n=int(input("n="))
for i in range (1, n+1):
    if check(i):
        print(i)
