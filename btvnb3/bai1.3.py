N= int(input("nhap N="))
list= [int(input(f"list[{i}]=")) for i in range(N)]
X= int(input("nhap X="))
print("so lan X xuat hien la",list.count(X))
list[1:7]= [8,5,4,0,1,3]
print(list)
print(max(list))
print(min(list))
Y= int(input("nhap Y="))
list.insert(0, Y)
print(list)
list1=sorted(list)
list2=sorted(list, reverse=True)
if list==list1:
    print("tang")
elif list==list2:
    print("giam")
else:
    print("no")
for i in range(1,N+1):
    list[i]= list[i-1]+ list[i]
print("List moi la:")
print(list)
new_list=[94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print(sorted(new_list))
for i in range(1,10):
    if new_list[i]<0:
        new_list[i]=new_list[i]*(-1)
print(sorted(new_list))