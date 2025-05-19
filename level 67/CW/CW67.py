class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname =surname

    def __str__(self):
        return f"Name: {self.name}, surname: {self.surname}"
    
    def dads_name(self, name):
        return f"my dads surname is {self.surname} and the name {self.name}"
    
dad = Person("messi", "lionel")
me = Person("ronaldo", "cristiano")

print(me)
print(dad.dads_name("messi"))
