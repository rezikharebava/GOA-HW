#davaleba 1
list_of_name = ["Gurami", "Nika", "lika", "Anano"]

name_to_count = "Gurami"
count = list_of_name.count(name_to_count)

print(f"name'{name_to_count}' list {count}-ჯერ გვხვდება")


#davaleba 2 
list_of_numbers = [1, 2, 3, 4, 5]
list_of_numbers.reverse()
print("შებრუნებული სია:", list_of_numbers)


#davaleba 3
list_of_numbers = [1, 2, 3]
repeated_list = list_of_numbers * len(list_of_numbers)
print("სიის გამეორებული ელემენტები:", repeated_list)


#davaleba 4
insert_arr = ["Python", "Java", "C++"]
insert_arr.insert(1, "დავითი")
print("განახლებული სია:", insert_arr)


#davaleba 5
list_of_numbers = [1, 2, 3, 1, 4, 1]
element_to_count = 1
count = list_of_numbers.count(element_to_count)
list_of_numbers.remove(element_to_count)
print(f"ელემენტი '{element_to_count}' სიაში {count}-ჯერ გვხვდება.")
print("განახლებული სია:", list_of_numbers)