from typing import Any
from typing import Dict
from typing import List

from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(operations_data: List[Dict[str, Any]], filter_state: str) -> None:
    result_filtered = filter_by_state(operations_data, state=filter_state)
    state_exists = any(item.get("state") == filter_state for item in operations_data)
    if state_exists:
        assert all(item["state"] == filter_state for item in result_filtered)
    else:
        assert result_filtered == []


# Тесты для sort_by_date


def test_sort_by_date_descending(sort_by_date_data: List[Dict[str, Any]]) -> None:
    """Проверка сортировки по убыванию."""
    result = sort_by_date(sort_by_date_data)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sort_by_date_data: List[Dict[str, Any]]) -> None:
    """Проверка сортировки по возрастанию."""
    result = sort_by_date(sort_by_date_data, reverse=False)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=False)


def test_sort_by_date_double(sort_by_date_double_data: List[Dict[str, Any]]) -> None:
    """Проверка дубликатов и сохранения списка."""
    result = sort_by_date(sort_by_date_double_data)
    all_dates = [d["date"] for d in result]
    double_ids = [d["id"] for d in result if all_dates.count(d["date"]) >= 2]
    assert len(double_ids) >= 2 and double_ids == sorted(double_ids)


def test_sort_by_date_empty() -> None:
    """Пустой список."""
    assert sort_by_date([]) == []
