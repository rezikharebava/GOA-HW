#HW 1
def vowel_one(s):
    vowels = "aeiouAEIOU"
    return "".join("1" if char in vowels else "0" for char in s)

#HW 2
def reduce_fraction(fraction: tuple) -> tuple:
    a, b = fraction
    
    def get_node(a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a
    
    nod = get_node(a, b)
    return (a // nod, b // nod)

#HW 3
def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isalpha() or char.isdigit():
            count += 1
    return count

#HW 4
def solution(string, ending):
    if len(ending) > len(string):
        return False
    for i in range(1, len(ending) + 1):
        if string[-i] != ending[-i]:
            return False
    return True

#HW 5
def elimination(arr):
    seen = set()  
    for num in arr:
        if num in seen:
            return num  
        seen.add(num) 
    return None  