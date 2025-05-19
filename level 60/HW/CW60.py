# HW 1
def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result

# HW 2
def get_age(age):
    #your code here
    return int(age[0])


# HW 3
def feast(beast, dish):
    beast_first_letter = beast[0]
    beast_last_letter = beast[-1]
    dish_first_letter = dish[0]
    dish_last_letter = dish[-1]
    
    if beast_first_letter == dish_first_letter and beast_last_letter == dish_last_letter:
        return True
    else:
        return False

# HW 4
def array_plus_array(arr1, arr2):
    total = 0
    for num in arr1:
        total += num
    for num in arr2:
        total += num
    return total

# HW 5
def solution(number):
    if number < 0:
        return 0
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total