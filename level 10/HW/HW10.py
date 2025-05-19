#davaleba 1
age = int(input("what is youre age: "))

for i in range(age):
    print(f"ცვლადი {i + 1} მნიშვნელობა: {i}")

#davaleba 2
def cel_to_fra (c):
    return (9/5) +32

print(cel_to_fra(25))

#davaleba 3
#შედარებითი ოპერატორები
#ეს არის ტოლობის ოპერატორი
#მაგალითი
a = 10
b = 10
result = a == b

print(result)

#ეს არის უმცირესი ოპერატორი 
#მაგალითი
a = 5
b = 20
result = a < b

print(result)

#ეს არის არასწორი ოპერატორი
#მაგალითი
a = 4
b = 100
result = 4 != 100
print(result)

#3 ლოგიგური ოპერატორი
#and ოპერატორი
#მაგალითი
a = True 
b = False

result = a and b

print(result)

#or ოპერატორი 
#მაგალითი
a = True 
b = False

result = a or b

print(result)

#not ოპერატორი
#მაგალითი
a = True 
b = False

result = (not b)

print(result)

#davaleba 4
height = 5

for i in range(1, height + 1):
    print('*' * i)

#davalebaა 5
age = 20  
is_twenty = (age == 20)

if is_twenty:
    print("user is 20 years old")
else:
    print("user isnt 20 years old")