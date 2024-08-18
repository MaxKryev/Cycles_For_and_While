import numpy

"""
Практика часть 10
"""


def get_prime(number: int) -> list:
    prime_nums = []
    for num in range(2, 51):
        if num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3):
            prime_nums.append(num)
    return prime_nums


result = get_prime(number=50)
print(*result)

"""
Практика часть 11
"""

print(sum([i ** 2 for i in range(1, 11)]))

"""
Практика часть 12
"""

y = []
for x in numpy.arange(1, 11, 0.5):
    y.append(x**2)
print(*y)

"""
Практика часть 13
"""
factorials = []
n = 1
fact = 1
while n < 6:
    fact *= n
    factorials.append(fact)
    n += 1
print(*factorials)


