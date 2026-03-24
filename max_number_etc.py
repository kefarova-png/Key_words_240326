def max_number(a, b):
    if a >= b:
        return a
    return b


def empty_function():
    pass


def even_numbers(n):
    for number in range(0, n + 1):
        if number % 2 == 0:
            yield number


def test_max_number():
    def test_max_number():
        assert max_number(3, 2) == 3, "Ошибка: max_number(3, 2) должен быть равен 3"
        assert max_number(-1, 1) == 1, "Ошибка: max_number(-1, 1) должен быть равен 1"
        assert max_number(-111.5, -125.1) == -111.5, "Ошибка: max_number(-111.5, -125.1) должен быть равен -111.5"
        assert max_number(-1.5, 0) == 0, "Ошибка: max_number(-1.5, 0) должен быть равен 0"


try:
    a = float(input("Введите первое число и нажмите Enter  "))
    b = float(input("Введите второе число и нажмите Enter  "))
    max_number = max_number(a, b)
    print(f"Результат поиска максимального числа:\n{max_number}")
    n = int(input("Введите число-ограничитель и нажмите Enter  "))
    print(f"Все чётные числа от 0 до {n} включительно:")
    for number in even_numbers(n):
        print(number)
except ValueError:
    print("Ошибка: введено не число. В следующий раз введите, пожалуйста, число!")


test_max_number()
print("Все тесты пройдены!")

