from mypy.types import AnyType


def filter_by_state(filter_list: list[dict[str, AnyType]], state: str = "EXECUTED") -> list[dict[str, AnyType]]:
    """ "Функция, которая фильтрует список словарей по заданному ключу и значению"""
    value_executed = []

    for dict_meaning in filter_list:
        for key, value in dict_meaning.items():
            if key == "state" and value == state:
                value_executed.append(dict_meaning)
    return value_executed


def sort_by_date(sort_date: list[dict[str, AnyType]]) -> list[dict[str, AnyType]]:
    """ "Функция, которая сортирует список словарей по дате"""
    return sorted(sort_date, key=lambda x: str(x.get("date")), reverse=True)
