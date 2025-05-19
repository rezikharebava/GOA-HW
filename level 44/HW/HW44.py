#დავალება 1
def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    else:
        return False

print(validate_pin("1234"))  
print(validate_pin("12345")) 
print(validate_pin("a234"))  

#დავალება 2
ver gavakete

#დავალება 3
def binary_array_to_number(arr):
    return int(''.join(map(str, arr)), 2)

print(binary_array_to_number([0, 0, 0, 1]))  
print(binary_array_to_number([0, 0, 1, 0]))  
print(binary_array_to_number([0, 1, 0, 1]))  
print(binary_array_to_number([1, 0, 0, 1]))  
print(binary_array_to_number([0, 0, 1, 0]))  
print(binary_array_to_number([0, 1, 1, 0]))  
print(binary_array_to_number([1, 1, 1, 1]))  
print(binary_array_to_number([1, 0, 1, 1])) 

#დავალება 4
def min_max(lst):
    return [min(lst), max(lst)]

print(min_max([1, 2, 3, 4, 5]))  
print(min_max([2334454, 5]))  

#დავალება 5
def divisors(n):
    divisors_list = []
    
    for i in range(2, n):
        if n % i == 0:
            divisors_list.append(i)
    
    if len(divisors_list) == 0:
        return f"{n} is prime"
    else:
        return divisors_list

print(divisors(12)) 
print(divisors(25))  
print(divisors(13)) 