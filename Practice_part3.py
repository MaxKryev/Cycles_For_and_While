def get_average(number: int) -> float:
    """
    Функция возвращает среднее значение элемментов списка
    """
    lst = []
    while True:
        number = int(input("Введите число: "))
        if number == 0:
            break
        lst.append(number)
    average = sum(lst) / len(lst)
    return average


result = get_average(number=int)
print("Среднее значение: ", round(result, 2))
