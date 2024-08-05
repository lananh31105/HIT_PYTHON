n=int(input())
tuple=(input() for i in range(n))
for i in range(0,len(tuple)):
    tuple.count(tuple(i))==5
    print(tuple(i))


