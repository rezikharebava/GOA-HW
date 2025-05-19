#დავალება 1
def digitize(n):
    return [int(digit) for digit in str(n)][::-1]


#დავალება 2
def is_anagram(test, original):
    test = test.replace(" ", "").lower()
    original = original.replace(" ", "").lower()
    return sorted(test) == sorted(original)


#დავალება 3
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels: 
            count += 1


#დავალება 4