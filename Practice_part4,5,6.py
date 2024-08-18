import random
"""
Практика часть 4
"""
for i in range(101):
    print(i)

"""
Практика часть 5
"""
for a in range(10):
    for b in range(1, 10):
        print(f"{a} * {b} = {a*b}")

"""
Практика часть 6
"""
lst = [random.randint(-100, 100) for i in range(10)]
for i in range(len(lst)):
    print(lst[i])


def get_dict() -> dict:
    my_dict = {}
    for i in range(1, 10):
        my_dict["key" + str(i)] = random.randrange(-100, 100)
    return my_dict


result = get_dict()

for key in result:
    print(key, result[key])

