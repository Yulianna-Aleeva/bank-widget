import re
from collections import Counter
from typing import Any, Dict, List

OperationsList = List[Dict[str, Any]]


def filter_by_state(operations: OperationsList, state: str = "EXECUTED") -> OperationsList:
    """Фильтрует список операций по статусу.
    Args:
        operations (OperationsList): Список операций.
        state (str, optional): Статус для фильтрации. По умолчанию "EXECUTED".
    Returns:
        OperationsList: Отфильтрованный список."""
    return [item for item in operations if item.get("state") == state]


def sort_by_date(operations: OperationsList, reverse: bool = True) -> OperationsList:
    """Сортирует список операций по дате.
    Args:
        operations (OperationsList): Список операций.
        reverse (bool, optional): Порядок сортировки. По убыванию, если True.
    Returns:
        OperationsList: Отсортированный список."""
    return sorted(operations, key=lambda d: str(d.get("date", "")), reverse=reverse)


def process_bank_search(data: OperationsList, search: str) -> OperationsList:
    """Ищет подстроку во всех полях операций.
    Args:
        data (OperationsList): Список операций.
        search (str): Строка для поиска.
    Returns:
        OperationsList: Список операций, где найдена строка."""

    pattern = re.compile(re.escape(search), re.IGNORECASE)

    def match_in_item(item: Dict[str, Any]) -> bool:
        for value in item.values():
            if pattern.search(str(value)):
                return True
        return False

    return [item for item in data if match_in_item(item)]


def process_bank_operations(data: OperationsList, categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций по категориям.
    Args:
        data (OperationsList): Список операций.
        categories (List[str]): Список категорий для подсчета.
    Returns:
        Dict[str, int]: Словарь с количеством операций по каждой категории."""
    counter: Counter[str] = Counter()
    for item in data:
        if "description" in item:
            desc = str(item["description"]).lower()
            for category in categories:
                if category.lower() in desc:
                    counter[category] += 1
    return dict(counter)
