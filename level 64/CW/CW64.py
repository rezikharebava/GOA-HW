#CW 1
def make_upper_case(input_string):
    return input_string.upper()

#CW 2 
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


#CW 3
class = MyCat:
    x = cat

p1 = MyCat
print(p1.x)


#CW 4
class = human:
    def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

p1 = Person("rezi", "kharebava", 15)

print(p1.name, p1.surname, p1.age)


#CW 5
class = human:
    def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

    def __str__(self, name, surname, age):
        return f"{self.name} {self.surname} {self.age}"

    def My_name(self):
        return f"ჩემი სახელია{self.name}  

    def my_surname(self):
        return f"ჩემი გვარია{self.surname}"

    def My_age(self):
        return f"მე ვარ{self.age} წლის"


p1 = human("rezi", "kharebava", 15)

print(p1.name, p1.surname, p1.age)
print(P1.My_name())
print(P1.my_surname())
print(P1.My_age())