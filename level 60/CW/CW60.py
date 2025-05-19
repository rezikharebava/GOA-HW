#CW 1
def count_arara(n):
    if  n == 1:
        return "anane"
    result  = "adak " * (n // 2)
    
    if n % 2 == 1:
        result += "anane "
    return result.rstrip()

#CW 2

ვერ გავაკეთე

#CW 3
def max_possible_score(questions, new):
    new_set = set(new)
    total_score = 0
    
    for question, points in questions.items():
        if question in new_set:
            total_score += points * 2
        else:
            total_score += points
    
    return total_score
