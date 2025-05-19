# davaleba 1
letters = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო', 'პ', 'ჟ', 'რ', 'ს', 'ტ', 'უ', 'ფ', 'ღ', 'ქ', 'ჟ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']
vowels = ['ა', 'ე', 'ი', 'ო', 'უ']
vowel_count = sum(1 for letter in letters if letter in vowels)
print(f"ხმოვნების რაოდენობა სიაში: {vowel_count}")

# davaleba 2
multiples = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]
print("5-ის და 3-ის ჯერადები 1-დან 100-მდე:", multiples)

# davaleba 3
mixed_list = ['ა', 'ბ', '1', '2', 'გ', 'დ', '3']
combined_string = ''.join(map(str, mixed_list))
print("გაერთიანებული სტრინგი:", combined_string)

# davaleba 4
rows = 4
for i in range(rows):
    print(' ' * i + '******')

# davaleba 5
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if age > 12:
    print("შენ არ ხარ 12 წლის")
else:
    print("თქვენი ასაკი 12 ან ნაკლებია")