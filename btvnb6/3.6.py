def calculate(*args,operation):
    result = 0
    if operation =="add":
        for i in args:
            result +=i
    elif operation =="multiply":
        result= result+1
        for i in args:
            result *=i
    elif operation =="max":
        result =  max(args)
    elif operation=="min":
        result = min(args)    
    else: return "Invalid operation"
    return result
    
a = calculate(1,3,7,operation="max")
print(a)
