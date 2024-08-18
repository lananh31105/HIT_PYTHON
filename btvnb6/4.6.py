def kqua(number:int):
    sum = 0
    while number>0:
        sum=sum+number%10
        number=number//10
    return sum

n=int(input())
sum=kqua(n)
buoc=1
while True:
    buoc=buoc+1
    if sum>9:
        sum=kqua(sum)
    else: break

print(sum)
print(buoc)

