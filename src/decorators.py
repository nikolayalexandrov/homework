import time


def log(filename = None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:

                result = func(*args, **kwargs)

                name_func = func.__name__
                if filename:
                    with open(filename, 'a', encoding="utf-8") as file:
                        file.write(f"Функция {name_func} ок. Результат: {result}")
                        file.close()
                    return None
                else:
                    print(f"Функция {name_func} ок. Результат: {result}")
                    return None
            except Exception as e:
                name_func = func.__name__
                if filename:
                    file = open(filename, 'a', encoding='utf-8')
                    file.write(f"Ошибка выполнения - {name_func} error: {e}. Inputs: {args}, {kwargs}\n")
                    file.close()
                    return f"Ошибка выполнения {name_func} error: {e}. Inputs: {args}, {kwargs}\n"
                else:
                    print(f"Ошибка выполнения - {name_func} error: {e}. Inputs: {args}, {kwargs}\n")
        return wrapper
    return my_decorator

#@log(filename="mylog.txt")
# @log()
# def my_function(x, y):
#     return x + y
#
# my_function(2, 3)

@log()
def second_fun(x,y):
    return x / y

second_fun(3, "1")

