# HW 1

def first_non_consecutive(arr):
    if len(arr) < 2:
        return None

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    
    return None

# HW 2

def to_alternating_case(string):
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

# HW 3

def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')
    pass