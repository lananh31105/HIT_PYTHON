def dem(s):
    dict = {}
    for a in s:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1
    return dict

s = input()

dict1 = dem(s)
print(dict1)

