d = {"n":1500,
     "m":2,
     "CLUSTERS":3,
     "ITER":10000,
     "METHOD":"FCM",
     "MEASURE":"EUCLIDEAN",
     "YEARS":51}
# print(d)

# d["MEASURE"]="MANHATAN"
# print(d)

# print(d["METHOD"])

# d["LOSS FUNCTION"]="NORM_2"
# print(d)

# d.pop("YEARS")
# print(d)

s=input()   
for key, value in d.items():
    if s == value:
        print("trung")
        break
else:
    print("khong trung")

# set1=[]
# for key, value in d.items():
#     set1.append(value)
# set1=set(set1)
# print(set1)

# list1=[]
# for key, value in d.items():
#     list1.append(key)
#     list1.append(value)
# list1=list(list1)
# print(list1)