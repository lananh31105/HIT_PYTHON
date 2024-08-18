def format_phone_number(number):
    new_number = ''.join(filter(str.isdigit, number))    
    if len(new_number) == 10 and new_number[0] == 0:
        return new_number
    else: return 'Invalid phone number'
number = str(input())
print(format_phone_number(number))