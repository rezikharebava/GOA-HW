#davaleba 1
name = "two towers"  
result = "" 

for i in name:
    result += i
    print(i)
print(result)


#davaleba 2
number = int(input("გთხოვთ შეიყვანეთ ციფრი: "))  

if number % 2 == 0:
    print(f"{number} არის ლუწი")
else:
    print(f"{number} არის კენტი")


#davaleba 3
for number in range(1, 101):  
    if number % 2 == 0:
        print(f"{number} არის ლუწი")
    else:
        print(f"{number} არის კენტი")
