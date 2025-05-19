#დავალება 1
def sum_mix(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum
#დავალება 2
def double_char(s):
    ls = s.split(" ")
    ls3 = []
    for i in ls:
        ls2 = []
        for j in i:
            ls2.append(j)
            ls2.append(j)
        ls3.append("".join(ls2))
    return "  ".join(ls3)

#დავალება 3
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

#დავალება 4
def reverse_words(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.insert(0, word)  
    return ' '.join(reversed_words)

print(reverse_words("The greatest victory is that which requires no battle"))

#დავალება 5
def sum_str(a, b):
    if not a: a = "0"
    if not b: b = "0"
    
    return str(int(a) + int(b))


print(sum_str("4", "5"))   
print(sum_str("34", "5")) 
print(sum_str("", ""))     
print(sum_str("2", ""))    
print(sum_str("-5", "3"))  