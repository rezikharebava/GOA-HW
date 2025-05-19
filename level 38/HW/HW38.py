#davaleba1

set_1 = {10, 20, 30, 40}
set_2 = {50, 60, 70, 80}

print("Initial sets:")
print("set_1:", set_1)
print("set_2:", set_2)


set_1.add(50)  
print("\nAfter adding 50 to set_1:", set_1)


set_1.remove(20) 
print("\nAfter removing 20 from set_1:", set_1)


set_1.clear()  
print("\nAfter clearing set_1:", set_1)


set_1 = {10, 20, 30, 40}


difference_set = set_1.difference(set_2) 
print("\nDifference between set_1 and set_2:", difference_set)


union_set = set_1.union(set_2)  
print("\nUnion of set_1 and set_2:", union_set)

#davaleba2
student_info = {
    "რეზი":"name",
    "ხარებავა":"surname",
     14 :"age",
     100:"minimum_grade"
}

key = student_info.keys()
print("student რეზი ხარებავა info: ", key)

#davaleba3
students_data = {
    "name" : "რეზი",
    "surname" : "ხარებავა",
    "year" : 2010
}

z = students_data.values()
print(z)

#davaleba4
def AddToDatabase(first_name, last_name, age):
    database = {
        "name" = name,
        "surname" = surname,
        "age" = age
}
    return database

print(AddToDatabase("რეზი", "ხარებავა", 14))