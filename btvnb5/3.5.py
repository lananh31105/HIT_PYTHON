import random
list=['CNTT','KHMT','KTPM','HTTT']
n=int(input("so sinh vien la "))
msv=[input() for i in range(n)]
for i in range(n):
    d={f"Account{i+1}":
        {"Username":msv[i] ,"Password": f"{random.choice(list)}"+msv[i]}
    }
    print(d)