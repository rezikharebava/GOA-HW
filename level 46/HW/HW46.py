#დავალება 1
def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"

#დავალება 2
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        is_valid = True
        for i in range(len(pin)):
            if pin[i] < '0' or pin[i] > '9':
                is_valid = False
                break 
        
        if is_valid:
            return True
        else:
            return False
    else:
        return False

#დავალება 3
def odd_or_even(arr):
    if not arr:
        arr = [0]
    
    total_sum = sum(arr)
    
    if total_sum % 2 == 0:
        return "even"
    else:
        return "odd"
pass

#დავალება 4
def solution(nums):
    if not nums:  
        return []
    return sorted(nums)  

nums = [1, 2, 3, 10, 5]
print(solution(nums))

#დავალება 5
def greet(name):
    if not name:
        return "Hello World!"
    
    first_letter = name[0].upper()
    rest_of_name = name[1:].lower()
    capitalized_name = first_letter + rest_of_name
    
    greeting = "Hello " + capitalized_name + "!"
    
    return greeting