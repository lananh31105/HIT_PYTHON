n=int(input())
set= {int(input()) for i in range(n)}
m=int(input())
while sum(set)>m:
    set.remove(max(set))
print(set)
