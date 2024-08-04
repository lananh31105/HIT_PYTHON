n=int(input("n="))
m=int(input("m="))
list= [input() for i in range(n)]
print("cac so yeu thich la")
seta= {input() for i in range(m)}
print("cac so khong thich la")
setb= {input() for i in range(m)}
hp=0
for i in range(n):
    if list[i] in seta:
        hp=hp+1
    elif list[i] in setb:
        hp=hp-1
    else: hp=hp
print("muc do hanh phuc la ",hp)