#დავალება 1
def points(game):
    res = 0
    for score in game:
        if score[0] > score[2]:
            res +=3
        elif score[0] > score[2]:
            res += 0
        else:
            res += 1
    return res


#დავალება 2
age = 14
binary_age = ""

while age > 0:
    binary_age = str(age % 2) + binary_age
    age = age // 2

print(binary_age)
