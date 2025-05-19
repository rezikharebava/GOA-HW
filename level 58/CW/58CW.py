#task 1
def longest_word(s):
    words = s.split()
    longest_word = ""

    for word in words:
        if len(word) >= len(longest_word):
            longest_word = word

    return longest_word


print(longest_word("red white blue"))
print(longest_word("red blue gold"))
