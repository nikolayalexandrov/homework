import datetime
import logging
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который будет автоматически логировать начало и конец выполнения функции,
 а также ее результаты или возникшие ошибки.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            if filename:
                handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
            else:
                handler = logging.StreamHandler()

            formatter = logging.Formatter(
                fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            start_time = datetime.datetime.now()
            logger.info(f"Функция начата. Аргументы: {args}, Именованные аргументы: {kwargs}")

            try:
                result = func(*args, **kwargs)
                duration = datetime.datetime.now() - start_time
                logger.info(
                    f"Функция успешно завершена. "
                    f"Результат: {result}. "
                    f"Время выполнения: {duration.total_seconds():.3f} секунд"
                )
                return result

            except Exception as e:
                duration = datetime.datetime.now() - start_time
                logger.error(
                    f"Ошибка выполнения функции: {type(e).__name__}: {str(e)}. "
                    f"Время выполнения до ошибки: {duration.total_seconds():.3f} секунд",
                    exc_info=True,
                )
                raise

            finally:
                logger.removeHandler(handler)

        return wrapper

    return decorator
