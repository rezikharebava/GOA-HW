#HW 1
class = Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def Car_info(self):
        return f"Car name is{self.name} and model is {self.model} and age of the car is {self.age} "

CAR = Car ("Nissan", "GTR R35", 2012)

print(Car.Car_info())

#HW 2
class = Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.garde = garde

    def __str__(self,name, age, grade):
        return f"{self.name} {self.age} {self.garde}"
    
    def is_passing(self):
        if self.grade >= 10:
            print("you passed this test")
        else:
            print("you didin't pass")

grade = Student("rezi", "15", 10)
print(grade.is_passing())

#HW 3
class = Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        if self.age <= 4:
            print("Woolf!")
        else:
            print("no Woolf!")

bark = Dog("LUXY","3")
print(bark.bark())

#HW4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
         return self.height * self.width

areat = Rectangle(10, 20)
print(areat.area())

#HW 5
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Book title is {self.title} and author of this book is {self.author} and it was relised in {self.year}"

book = Book("ოთხმოცი ათასი კილომეტრი წყლის ქვეშ", "Jules Verne", "1871")
print(book.book-info())