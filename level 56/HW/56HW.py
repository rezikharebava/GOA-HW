# HW 1
def solution(string, ending):
    if len(ending) > len(string):
        return False
    for i in range(1, len(ending) + 1):
        if string[-i] != ending[-i]:
            return False
    return True

print(solution('abc', 'bc'))  
print(solution('abc', 'd')) 

# HW 2
def even_or_odd(s):
    even_sum = sum(int(d) for d in s if int(d) % 2 == 0)
    odd_sum = sum(int(d) for d in s if int(d) % 2 != 0)
    
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
    
# HW 3
def even_numbers(arr, n):
    return [x for x in arr if x % 2 == 0][-n:]

# HW 4
def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    indices = []
    
    for index, char in enumerate(word, start=1):
        if char in vowels:
            indices.append(index)
    return indices

# HW 5
def geometric_sequence_elements(a, r, n):
    sequence = []
    
    for i in range(n):
        sequence.append(str(a * r**i))
    return ', '.join(sequence)