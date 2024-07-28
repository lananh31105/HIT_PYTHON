s1=input("s1: ")
s2=input("s2: ")
print(s1[::-1])
a=int(input("a="))
b=int(input("b="))
if 1<=a and a<b and b<=len(s2):
    new_s2=s2[a:b+1]
    print(new_s2[::-1])
else:
    print("no")
s3=" "
for i in range(len(s1)):
    if i%2!=0:
        s3=s3+s1[i]
print(s3)
max=max(len(s1),len(s2))
s4=" "
for i in range(max):
    if (i < len(s1)):
        s4 += s1[i]
    if (i < len(s2)):
        s4 += s2[i]
print(s4)
s1_1=s1[0]
s2_1=s2[0]
news1= s2_1+ s1[1:]
news2= s1_1+ s2[1:]
print(news1, news2)