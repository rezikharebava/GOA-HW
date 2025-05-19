# clsswork 1
def is_isogram(string):
    lower_string = string.lower()
    char_counts = [lower_string.count(char) for char in lower_string]
    return all(count == 1 for count in char_counts)