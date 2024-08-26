k= int(input("k="))
dem=0
for i in range(1,500):
    sum=0
    i1=i
    while i>0:
        sum+=i%10
        i=i//10
    if sum==10:
        dem+=1
    if dem==k:
        print(i1)
        break