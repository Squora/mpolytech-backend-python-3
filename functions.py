"""
Модуль с примерами различных типов функций в Python.
"""

def greet():
    """
    Функция без параметров.
    Возвращает приветственное сообщение.
    """
    return "Hello, world!"


def greet_user(name):
    """
    Функция с параметром.
    Возвращает приветственное сообщение пользователю.
    
    Args:
        name (str): Имя пользователя.
        
    Returns:
        str: Приветственное сообщение.
    """
    return f"Hello, {name}!"


def greet_user_with_time(name, time_of_day="morning"):
    """
    Функция с несколькими параметрами со значениями по умолчанию.
    
    Args:
        name (str): Имя пользователя.
        time_of_day (str, optional): Время суток (по умолчанию: "morning").
        
    Returns:
        str: Приветствие с указанием времени суток.
    """
    return f"Good {time_of_day}, {name}!"


def multiply(a: int, b: int) -> int:
    """
    Функция с несколькими параметрами, у которых задан тип.
    
    Args:
        a (int): Первый множитель.
        b (int): Второй множитель.
        
    Returns:
        int: Результат умножения a на b.
    """
    return a * b


def sum_numbers(*args):
    """
    Функция с неопределённым количеством параметров (args).
    
    Args:
        *args: Произвольное количество чисел.
        
    Returns:
        int: Сумма всех переданных чисел.
    """
    return sum(args)


def print_user_info(**kwargs):
    """
    Функция с неопределённым количеством параметров (kwargs).
    
    Args:
        **kwargs: Произвольные именованные параметры.
        
    Prints:
        Информацию о пользователе в формате "ключ: значение".
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def outer_function():
    """
    Функция, вызывающая внутри себя другую функцию.
    
    Returns:
        str: Сообщение от внутренней функции.
    """
    def inner_function():
        """
        Внутренняя функция.
        
        Returns:
            str: Сообщение от внутренней функции.
        """
        return "Hello from the inner function!"
    
    return inner_function()


def execute_function(func):
    """
    Функция, принимающая другую функцию в качестве аргумента.
    
    Args:
        func (function): Функция для выполнения.
        
    Returns:
        Результат выполнения переданной функции.
    """
    return func()


def say_hello():
    """
    Функция возвращает приветственное сообщение.
    
    Returns:
        str: Приветствие.
    """
    return "Hello!"


def say_goodbye():
    """
    Функция возвращает прощальное сообщение.
    
    Returns:
        str: Прощание.
    """
    return "Goodbye!"


def outer_with_local():
    """
    Функция с объявленной внутри локальной функцией.
    
    Returns:
        str: Результат выполнения локальной функции.
    """
    def local_func():
        """
        Локальная функция.
        
        Returns:
            str: Результат выполнения.
        """
        return "Local function result"
    
    return local_func()


def another_outer_with_local():
    """
    Функция с объявленной внутри локальной функцией с параметром.
    
    Returns:
        int: Результат выполнения локальной функции.
    """
    def local_func(x):
        """
        Локальная функция умножает параметр на 2.
        
        Args:
            x (int): Входное значение.
            
        Returns:
            int: Удвоенное значение.
        """
        return x * 2
    
    return local_func(5)


no_param_lambda = lambda: "No parameters here"
"""
Лямбда-выражение без параметров.
"""


square = lambda x: x ** 2
"""
Лямбда-выражение с параметром.
"""


def apply_lambda(func, value):
    """
    Функция, принимающая лямбда-выражение как параметр.
    
    Args:
        func (function): Лямбда-выражение.
        value: Входное значение для лямбда-выражения.
        
    Returns:
        Результат выполнения лямбда-выражения.
    """
    return func(value)


def outer_closure(x):
    """
    Функция с замыканием.
    
    Args:
        x (int): Входное значение.
        
    Returns:
        function: Внутренняя функция, увеличивающая x на 1.
    """
    def inner():
        return x + 1
    
    return inner


def create_multiplier(factor):
    """
    Функция с замыканием, создающая множитель.
    
    Args:
        factor (int): Множитель.
        
    Returns:
        function: Внутренняя функция, умножающая входное значение на множитель.
    """
    def multiplier(x):
        return x * factor
    
    return multiplier


def counter():
    """
    Функция с замыканием, создающая счетчик.
    
    Returns:
        function: Внутренняя функция, увеличивающая значение счетчика на 1.
    """
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment
