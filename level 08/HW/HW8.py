#davaleba 1
age = int(input("enter age:"))
print("age")

if age > 13 and age < 19:
    print("youre age is more than 13 and lower than 19")
else:
    print("youre age is acepted ")
#davaleba 2
grade = int(input("enter youre exem grade "))

is_A = grade >= 9
is_B = 8 <= grade <9
is_C = 7 <= grade <8
is_D = 6 <= grade <7
is_F = grade < 6

print("is_A:", is_A)
print("is_B",  is_B)
print("is_C",  is_C)
print("is_D",  is_D)
print("is_F",  is_F)

#davaleba 3
a = True
b = False

print("a and b", a and b)
print("a or b", a or b)
print("not b", not b)
print("not a", not a)
print("a or b", not a)  

#davaleba 4
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))


print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} != {num2}: {num1 != num2}")

#davaleba 5
a = 9
b = 5
c = 3

is_a_greatest = a > b and a > c
is_b_middle =(b > c and b < a) or (b < c and b > a)
is_c_least = c < a and c < b

print(f"a is biggest: {is_a_greatest}")
print(f"b is the middle: {is_b_middle}")
print(f"c is the lowest: {is_c_least}")

#davaleba 6
score = int(input("enter youre score between 0-100: "))

is_pass =  score > 50
is_hight_pass = score > 75, score < 95
is_perfect = score == 100
is_failing = score < 50

print("is_pass:", is_pass)
print("is_hight_pass:", is_hight_pass)
print("is_perfect:", is_perfect)
print("is_failing:", is_failing)

#davaleba 7
P = True
Q = False

P_and_not_Q = P and not Q
not_P_and_Q = Q and not P
P_xor_Q = (P or Q) and not (P and Q)

print("P_and_not_Q:", P_and_not_Q)
print("not_P_and_Q:", not_P_and_Q)
print("P_xor_Q:", P_xor_Q)