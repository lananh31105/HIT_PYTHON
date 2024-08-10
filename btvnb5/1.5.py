d={
    2023123456: 3.5,
    2022123789: 2.5,
    2020987654: 3.0,
    2019456321: 1.5,
    2021147852: 4.0,
}
a=0
for key, value in d.items():
    if value>=3.0 and value<=3.5:
        a=a+1
print(a)

d[2000123654]= 2.0
print(d)

dict1=[]
for key, value in d.items():
    if value<2.0:
        dict1.append(key)
for key in dict1:
    d.pop(key)
print(d)

d.clear()
print(d)