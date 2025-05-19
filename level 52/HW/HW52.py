# homework 1
def multi_table(number):
    table = []
    for i in range(1, 11):
        table.append(f"{i} * {number} = {i * number}")
    return "\n".join(table)#Good luck

number = 5
result = multi_table(number)
print(result)

# homework 2
def print_array(arr):
    return ','.join(map(str, arr))

# homework 3
def string_clean(s):
    return ''.join([char for char in s if not char.isdigit()])

# homework 4
def remove_consecutive_duplicates(s):
    splied_words = s.split(" ")
    result_arr = []
    for i in range(len(splied_words)):
        if (splied_words[i] != splied_words[i-1]) or (i == 0):
            result_arr.append(splied_words[i])
    return " ".join(result_arr)

# homework 5
def between_extremes(arr):
    return max(arr) - min(arr)

print(between_extremes([23, 3, 19, 21, 16])) 
print(between_extremes([1, 434, 555, 34, 112])) 
    