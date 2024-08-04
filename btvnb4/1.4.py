tuple1= ("0","1","3","4","5","7","9")
tuple1 = list(tuple1)
for i in range(0,len(tuple1)):
    tuple1[i] = int(tuple1[i])
tuple1 = tuple(tuple1)    
print(tuple1) 

