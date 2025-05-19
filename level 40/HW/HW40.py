#დავალება 1
def remove_duplicate_words(s):
    ls = s.split(" ")
    ls2 = []
    
    for i in ls:
        if i not in ls2:
            ls2.append(i)
    return " ".join(ls2)

# დავალება 2
def stray(arr):
    if arr[0] == arr[-1]:
        for i in arr:
            if i != arr[0]:
                return i
    else:
        if arr[0] == arr[1]:
            return arr[-1]
        else:
            return arr[0]

#დავალება 3
def solution(nums):
    if nums is None or nums == []:
        return []
    return sorted(nums)

#დავალება 4
def capitals(word):
    ls = []
    for i in range(len(word)):
        if word[i] == word[i].upper():
            ls.append(i)
    return ls

#დავალება 5
import math
def factorial(n):
    return math.factorial(n)