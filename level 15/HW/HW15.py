#davaleba 1
elements = []

elements.append(input("შეიყვანეთ თქვენი სახელი: "))
elements.append(input("შეიყვანეთ თქვენი ასაკი: "))
elements.append(input("შეიყვანეთ თქვენი ქალაქი: "))
elements.append(input("რა არის თქვენი საყვარელი ფერი: "))

elements.append("დამატებითი ინფორმაცია")

for element in elements:
    print(element)


#davaleba 2
numbers = [9, 5, 94, 711, 52, 96, 71, 8]
smallest_number = numbers[0]


for num in numbers:
    
    if num < smallest_number:
       
        smallest_number = num


print("ყველაზე პატარა რიცხვია:", smallest_number)