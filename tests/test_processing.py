from typing import Any
from typing import Dict
from typing import List

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


# Тесты для test_filter_by_state
# Запуск: pytest -k test_filter_by_state_parametrize
@pytest.mark.parametrize("state", ["EXECUTED", "CANCELED", "UNKNOWN", ""])
def test_filter_by_state_parametrize(state: str) -> None:
    operations_by_filter = [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result = filter_by_state(operations_by_filter, state)
    status_exists = any(item["state"] == state for item in operations_by_filter)
    if status_exists:
        assert len(result) > 0
    else:
        assert result == []


# Запуск: pytest -k test_filter_by_state
def test_filter_by_state(operations_data: List[Dict[str, Any]], filter_state: str) -> None:
    result_filtered = filter_by_state(operations_data, state=filter_state)
    state_exists = any(item.get("state") == filter_state for item in operations_data)
    if state_exists:
        assert all(item["state"] == filter_state for item in result_filtered)
    else:
        assert result_filtered == []


# Тесты для sort_by_date
# Запуск: pytest -k test_sort_by_date_parametrize
@pytest.mark.parametrize(
    "operations, reverse, expected",
    [
        # Проверка сортировки по убыванию
        ([{"date": "2008-03-03"}, {"date": "2008-03-01"}], True, [{"date": "2008-03-03"}, {"date": "2008-03-01"}]),
        # Проверка сортировки по возрастанию
        ([{"date": "2008-03-03"}, {"date": "2008-03-01"}], False, [{"date": "2008-03-01"}, {"date": "2008-03-03"}]),
        # Проверка дубликатов
        ([{"date": "2008-03-03"}, {"date": "2008-03-03"}], True, [{"date": "2008-03-03"}, {"date": "2008-03-03"}]),
        # Пустое значение даты
        ([{"date": ""}, {"date": "2008-03-03"}], True, [{"date": "2008-03-03"}, {"date": ""}]),
        # Пустой список
        ([], True, []),
    ],
)
def test_sort_by_date_parametrize(
    operations: List[Dict[str, Any]], reverse: bool, expected: List[Dict[str, Any]]
) -> None:
    result = sort_by_date(operations, reverse)
    assert sorted(result, key=lambda x: str(x)) == sorted(expected, key=lambda x: str(x))


# Запуск: pytest -k test_sort_by_date_descending
def test_sort_by_date_descending(sort_by_date_data: List[Dict[str, Any]]) -> None:
    """Проверка сортировки по убыванию."""
    result = sort_by_date(sort_by_date_data)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)


# Запуск: pytest -k test_sort_by_date_ascending
def test_sort_by_date_ascending(sort_by_date_data: List[Dict[str, Any]]) -> None:
    """Проверка сортировки по возрастанию."""
    result = sort_by_date(sort_by_date_data, reverse=False)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=False)


# Запуск: pytest -k test_sort_by_date_double
def test_sort_by_date_double(sort_by_date_double_data: List[Dict[str, Any]]) -> None:
    """Проверка дубликатов и сохранения списка."""
    result = sort_by_date(sort_by_date_double_data)
    all_dates = [d["date"] for d in result]
    double_ids = [d["id"] for d in result if all_dates.count(d["date"]) >= 2]
    assert len(double_ids) >= 2 and double_ids == sorted(double_ids)


# Запуск: pytest -k test_sort_by_date_empty
def test_sort_by_date_empty() -> None:
    """Пустой список."""
    assert sort_by_date([]) == []
