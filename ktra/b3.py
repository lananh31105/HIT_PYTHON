n=int(input("so luong nguoi tham gia la "))
list=[str(input()) for i in range(n)]
list.remove(min(list))
for i in range(n):
    if min(list)==list[i]:
        print(list[i])
