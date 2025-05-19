#davaleba1
def password(password):

    if len(password) < 8:
        return False
    

    if not any(char.isupper() for char in password):
        return False
    

    if not any(char.islower() for char in password):
        return False
    

    if not any(char.isdigit() for char in password):
        return False
    

    return True


print(password("Abcd1234"))
print(password("Abcd123"))
print(password("abcd1234"))
print(password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"))

#davaleba2
def is_isogram(s):
    s = s.lower()
    seen = set()
    
    for char in s:
        if char in seen:
            return False
        
        seen.add(char)

    return True

#davaleba3
def friend(x):
    return [name for name in x if len(name) == 4]


print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
print(friend(["Peter", "Stephen", "Joe"]))

#davaleba4
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False

print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("123456"))
print(validate_pin("12a4"))