#დავალება 1
def simple_multiplication(num):
    if num % 2 == 0:
        return num * 8
    else:
        return num * 9

#დავალება 2
def invert(numbers):
    return [-num for num in numbers]


#დავალება 3
def fake_bin(x):
    result = ""
    for digit in x:
        if int(digit) < 5:
            result += "0"
        else:
            result += "1"
    return result


#დავალება 4
def string_to_array(s):
    if s == "":
        return ['']
    return s.split()


#დავალება 5
def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "rock" and player2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"


#დავალება 6
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

    
#დავალება 7
def monkey_count(n):
    return (for i in range(1, n + 1))


#დავალება 8
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]

    elif human_years == 2:
        return [2, 24, 24]

    cat_years = 24 + (human_years - 2) * 4
    dog_years = 24 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))
print(human_years_cat_years_dog_years(5))


#დავალება 9
def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)


#davaleba 10
def binary_array_to_number(binary_array):
    return int(''.join(map(str, binary_array)), 2)