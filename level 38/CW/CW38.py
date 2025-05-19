#davaleba1
def manual_difference(set1, set2):
    result = set()
    for element in set1:
        if element not in set2:
            result.add(element)
    return result


set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}


print(manual_difference(set_a, set_b))


#davaleba2
student_1 = {
    "name": "გურამი",
    "gvari": "გელხაური",
    "age": 16,
    "საშვალო ქულა": 8
}
student_2 = {
    "name": "ლადო",
    "surname": "ნიჟარაძე",
    "age": 14,
    "საშუალო ქულა": 10
}
print(student_1)
print(student_2)