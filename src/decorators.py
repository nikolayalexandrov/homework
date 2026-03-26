


def log(filename=None):
    """Декоратор для логирования выполнения функции.
    Если задан `filename`, лог записывается в файл, иначе выводится в консоль"""

    def my_decorator(func):
        """Возвращает обёртку, которая логирует выполнение функции `func`"""

        def wrapper(*args, **kwargs):
            """Обёртка для выполнения функции `func` с логированием её результата и ошибок."""
            try:

                result = func(*args, **kwargs)

                name_func = func.__name__
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Функция {name_func} ок. Результат: {result}")
                        file.close()
                    # return None
                else:
                    print(f"Функция {name_func} ок. Результат: {result}")
                    # return None
            except Exception as e:
                result = None
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"Ошибка выполнения - {name_func} error: {e}. Inputs: {args}, {kwargs}\n")
                    file.close()
                    print(f"Ошибка выполнения {name_func} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    result = None
                    print(f"Ошибка выполнения - {name_func} error: {e}. Inputs: {args}, {kwargs}\n")
            return result

        return wrapper

    return my_decorator


# @log(filename="mylog.txt")
# @log()
# def my_function(x, y):
#     return x + y
#
# my_function(2, 3)


@log()
def second_fun(x, y):
    return x / y


second_fun(3, "1")
