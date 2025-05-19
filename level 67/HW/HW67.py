import math
#HW 1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Max", 5)
dog2 = Dog("Bella", 3)


print(f"Dog 1: Name - {dog1.name}, Age - {dog1.age}")
print(f"Dog 2: Name - {dog2.name}, Age - {dog2.age}")

#HW 2
class Car:
    def drive(self):
        print("The car is driving")
        
    def stop(self):
        print("The car has stopped")

my_car = Car()

my_car.drive()
my_car.stop()

#HW 3
#ver gavakete

#HW 4
class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def introduce(self):
        print(f"My name is {self.name}, I study {self.subject} and my grade is {self.grade}.")

student = Student("rezi", 15, "Math")

student.introduce()

#HW 5
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")


account = BankAccount(100)


account.deposit(50)
account.withdraw(30)
account.withdraw(200)