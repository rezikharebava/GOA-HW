#დავალება 1
def filter_list(lst):
    arr = []
    for item in lst:
        if type(item) == int and item >= 0:
            arr.append(item)
    return arr


#დავალება 2
def disemvowel(string):
    vowels = "aeiouAEIOU"
    result = []

    for char in string:
        is_vowel = False
        for vowel in vowels:
            if char == vowel:
                is_vowel = True
                break
        if not is_vowel:
            result.append(char)

    return ''.join(result)


#დავალება 3 
def descending_order(num):
    num_str = str(num)
    digits = []
    
    for char in num_str:
        digits.append(char)
    
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]

    sorted_num_str = ''.join(digits)
    return int(sorted_num_str)
