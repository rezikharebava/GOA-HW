#HW 1

double_char = lambda s: ''.join([c*2 for c in s])

#HW 2

get_average = lambda marks: sum(marks) // len(marks)

# homeowork 3

get_planet_name = lambda id: {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune"
}.get(id, "")

#HW 4

sum_str = lambda a, b: str(int(a or "0") + int(b or "0"))