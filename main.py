"""
Основной модуль для вызова функций из модуля functions.
"""

from functions import (greet, greet_user, greet_user_with_time, multiply, sum_numbers, 
                       print_user_info, outer_function, execute_function, say_goodbye, 
                       outer_with_local, another_outer_with_local, no_param_lambda, 
                       square, apply_lambda, counter, create_multiplier)


def main():
    """
    Главная функция для вызова примеров различных функций из модуля functions.
    """
    # Функция без параметров
    print(greet())

    # Функция с параметрами
    print(greet_user("Alice"))

    # Функция с несколькими параметрами со значениями по умолчанию
    print(greet_user_with_time("Alice", "evening"))

    # Функция с несколькими параметрами, у которых задан тип
    print(multiply(3, 4))

    # Функция с неопределённым количеством параметров (args)
    print(sum_numbers(1, 2, 3, 4, 5))

    # Функция с неопределённым количеством параметров (kwargs)
    print_user_info(name="Alice", age=25)

    # Функция, вызывающая внутри себя другую функцию
    print(outer_function())

    # Функция, принимающая функцию как параметр
    print(execute_function(say_goodbye))

    # Функции с объявленной внутри локальной функцией
    print(outer_with_local())
    print(another_outer_with_local())

    # Лямбда-выражения
    print(no_param_lambda())
    print(square(6))

    # Функция, принимающая лямбда-выражение как параметр
    print(apply_lambda(lambda x: x * 3, 7))

    # Примеры с замыканиями
    inc = counter()
    print(inc())
    print(inc())
    print(inc())

    multiply_by_3 = create_multiplier(3)
    print(multiply_by_3(5))

    input("Нажмите Enter, чтобы завершить программу...")


if __name__ == '__main__':
    main()
