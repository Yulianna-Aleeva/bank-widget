import re
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple

from constants import DATE_FORMATS
from src.processing import filter_by_state
# from src.processing import sort_by_date


def test_filter_by_state(operations_data: List[Dict[str, Any]], filter_state: str) -> None:
    result_filtered = filter_by_state(operations_data, state=filter_state)
    state_exists = any(item.get("state") == filter_state for item in operations_data)
    if state_exists:
        assert all(item["state"] == filter_state for item in result_filtered)
    else:
        assert result_filtered == []


# Тесты для sort_by_date


def filter_dates(data: List[Dict[str, Any]]) -> Tuple[List[str], List[str]]:
    valid, invalid = [], []
    for item in data:
        date = item.get("date", "")
        if any(re.fullmatch(pattern, date) for pattern in DATE_FORMATS):
            valid.append(date)
        else:
            invalid.append(date)
    return valid, invalid


# Сортировка по убыванию
def test_sort_by_date_down(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(operations, key=lambda d: d.get("date", ""), reverse=True)


# Сортировка по убыванию валидных дат
def test_sort_by_date_down_valid(valid: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(valid, key=lambda d: d["date"], reverse=True)


# Сортировка по возрастанию
def test_sort_by_date_up(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(operations, key=lambda d: d.get("date", ""))


# Сортировка по возрастанию валидных дат
def test_sort_by_date_up_valid(valid: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(valid, key=lambda d: d["date"])


# Дублирующиеся даты
def test_sort_by_date_double(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(operations, key=lambda d: (d.get("date", ""), d.get("id", "")))


# Дублирующиеся валидные даты
def test_sort_by_date_up_double(valid: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(valid, key=lambda d: (d["date"], d.get("id", "")))


# Не валидные даты
def test_sort_by_date_invalid(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(operations, key=lambda d: (d.get("date", "") == "", d.get("date", "")))
