#davaleba 1
name = input("enter your name: ")

result ="  ".join(name)

print(result)


#davaleba 2
start = int(input("შეიყვანეთ დიაპაზონის საწყისი: "))
end = int(input("შეიყვანეთ დიაპაზონის ბოლო: "))

for num in range(start, end + 1):
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} - ეს ციფრები არის 3-ისა და 2-ის ჯერადები")
    else:
        print(f"{num} - magaria")


#davaleba 3
result = 0

for i in range(5):
    num = int(input(f"შეიყვანეთ {i+1}-ე ციფრი: "))
    result += num  

average = result / 5

print(f"შეიყვანეთ ციფრების საშუალო არითმეტიკულია: {average} <3")


#davaleba 4
result = 0

for num in range(-100, 101):
    if num > 0:  
        result += num  

print(f"დადებითი რიცხვების ჯამი -100 დან 100 დე: {result}")


#davaleba 5
result = 0

while True:
    num = int(input("შეიყვანეთ დადებითი ციფრი (შეჩერებისთვის უარყოფითი): "))
    
    if num < 0:  
        print("თქვენ შეყვანეთ უარყოფითი რიცხვი. დასრულდა.")
    break
    
    result += num 

print(f"დადებითი რიცხვების ჯამი: {result}")


#davaleba 6
n = 10

for i in range(1, n+1):
    
    print('*' * n, end='')
    
    print(' ' * (2 * (i - i)), end='')
    
    print('*' * i)

