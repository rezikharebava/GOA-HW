#davaleba 1
def custom_split(string, delimiter=" "):
    result = []
    current_word = ""
    for char in string:
        if char == delimiter:
            if current_word:
                result.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        result.append(current_word)
    return result

#davaleba 2
def custom_join(delimiter, iterable):
    result = ""
    for i, item in enumerate(iterable):
        result += item
        if i < len(iterable) - 1:
            result += delimiter
    return result

#davaleba 3
def custom_replace(string, old, new):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += string[i]
            i += 1
    return result

#davaleba 4
def mini_calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Division by zero!"
    else:
        return "Unsupported operation!"

#davaleba 5
def add_words_to_array():
    word_count = int(input("რამდენი სიტყვა გსურთ დაამატოთ? "))
    words = []
    for _ in range(word_count):
        word = input("შეიყვანეთ სიტყვა: ")
        words.append(word)
    joined_words = custom_join(" ", words)
    print(f"დაჯგუფებული სიტყვები: {joined_words}")
    return words

if __name__ == "__main__":
  
    text = "Hello world this is Python"
    print("Split result:", custom_split(text))
    
    words = ["Hello", "world", "Python", "rocks"]
    print("Join result:", custom_join(" ", words))
    
    text = "Hello world, world is beautiful!"
    print("Replace result:", custom_replace(text, "world", "Earth"))
    
    print("Calculator result:", mini_calculator(10, 5, "+"))
    print("Calculator result:", mini_calculator(10, 0, "/"))
    
    add_words_to_array()