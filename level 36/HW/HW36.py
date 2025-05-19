#davaleba1
def filter_list(l):
    result = []
    for item in l:
        if isinstance(item, int):
            result.append(item)
    return result

print(filter_list([1, 2, 'a', 'b']))          
print(filter_list([1, 'a', 'b', 0, 15]))      
print(filter_list([1, 2, 'aasf', '1', '123', 123]))  

#davaleba2
def square_digits(num):
    result = ""
    for digit in str(num):
        squared = int(digit) ** 2
        result += str(squared)
    return int(result)

print(square_digits(9119))  
print(square_digits(765))   

#davaleba3
def get_middle(s):
    length = len(s)
    middle = length // 2
    
    if length % 2 == 0:  
        return s[middle - 1:middle + 1]
    else:  
        return s[middle]

print(get_middle("test"))     
print(get_middle("testing"))  
print(get_middle("middle"))   
print(get_middle("A"))  

#davaleba4
def find_short(s):
    words = s.split()
    shortest_length = len(words[0])  
    
    for word in words:
        if len(word) < shortest_length:
            shortest_length = len(word)
    
    return shortest_length


print(find_short("The quick brown fox")) 
print(find_short("I love Python programming"))  
print(find_short("Simple example test case"))  

#davaleba5
def solution(string, ending):
    if len(ending) > len(string):
        return False
    for i in range(1, len(ending) + 1):
        if string[-i] != ending[-i]:
            return False
    return True


print(solution('abc', 'bc'))  
print(solution('abc', 'd')) 