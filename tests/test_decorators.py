from contextlib import redirect_stdout
from io import StringIO

import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x + y


def test_my_function_console_output(capsys):
    my_function(2, 3)
    captured = capsys.readouterr()
    assert "Функция my_function ок." in captured.out


@log()
def my_function_2(x, y):
    return x - y

def test_my_function_console_output_2(capsys):
    my_function(3, 1)
    captured = capsys.readouterr()
    assert "Функция my_function ок." in captured.out


@log()
def my_function_1(a, b):
    return a / b

def test_error(capsys):
    with pytest.raises(Exception):
        my_function_1(3, 0)
        captured = capsys.readouterr()
        assert "Ошибка в second_fun: ZeroDivisionError, args: (3, 0), {}" in captured.out

@log()
def my_function_3(a, b):
    return a / b

def test_error_1(capsys):
    with pytest.raises(Exception):
        my_function_3(3, "1")
        captured = capsys.readouterr()
        assert "Ошибка выполнения - second_fun error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: (3, '1'), {}" in captured.out