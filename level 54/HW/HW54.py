# homework 1
def sort_by_length(arr):
    return sorted(arr, key=len)
    pass

# homework 2
def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    
    total = 0
    for i in range(begin_number, end_number + 1, step):
        total += i
    
    return total

    #your code here

# homework 3
def series_sum(n):
    sum = 0
    for x in range(n):
        sum = sum + 1/(3 * x + 1)
    return "%.2f" % sum
    # Happy Coding ^_^

# homework 4
def round_to_next5(n):
    return n if n % 5 == 0 else n + (5 - n % 5)
    pass

# homework 5
def two_oldest_ages(ages):
    return sorted(ages)[-2:]
    #your code here