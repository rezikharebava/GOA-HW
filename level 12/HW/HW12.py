#davaleba 1
for i in range(1, 50, 2):
    print("guram", i)

#davaleba 2
size = 5  

for i in range(size): 
    j = 0
    while j < size:  
        print("*", end=" ")
        j += 1
    print() 

#davaleba 3
height = 4  
width = 7   

for i in range(height): 
    j = 0
    while j < width:  
        print("*", end=" ")
        j += 1
    print() 

#davaleba 4
for num1 in range(1, 4): 
    for num in range(1, 4): 
        print(f"num1: {num1}, num: {num}") 

#davaleba 5

username = ""
email = ""
password = ""

while not username or not email or not password: 
    print("გთხოვთ, შეავსეთ სარეგისტრაციო ფორმა:")
    
    username = input("სახელი: ")
    if not username:
        print("სახელი სავალდებულოა.")
    
    email = input("ელ.ფოსტა: ")
    if not email or "@" not in email:  
        print("გთხოვთ, ჩაწერეთ სწორი ელ.ფოსტა.")
        email = ""  
    
    password = input("პაროლი: ")
    if len(password) < 6: 
        print("პაროლი უნდა")