#დავალება 1
def xo(s):
    return s.lower().count("x") == s.lower().count("o")

#დავალება 2
def find_short(s):
    words = s.split()
    shortest_word = min(words, key=len)
    return len(shortest_word)

#დავალება 3
def solution(text, ending):
    return text.endswith(ending)

#დავალება 4
def accum(s):
    result = []
    for i in range(len(s)):
        char = s[i]
        part = char.upper() + char.lower() * i  
        result.append(part)
    return '-'.join(result)