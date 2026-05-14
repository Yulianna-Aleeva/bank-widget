from typing import Any
from typing import Dict
from typing import List

import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


# Тесты для filter_by_currency
# Запуск: pytest -k test_filter_by_currency
@pytest.mark.parametrize("currency, expected_count", [("USD", 2), ("RUB", 1), ("EUR", 0)])
def test_filter_by_currency(sample_transactions: List[Dict[str, Any]], currency: str, expected_count: int) -> None:
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count


# Запуск: pytest -k test_filter_by_currency_empty
def test_filter_by_currency_empty() -> None:
    assert list(filter_by_currency([], "USD")) == []


# Тесты для transaction_descriptions
# Запуск: pytest -k test_transaction_descriptions
def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]


# Запуск: pytest -k test_transaction_descriptions_empty
def test_transaction_descriptions_empty() -> None:
    assert list(transaction_descriptions([])) == []


# Тесты для card_number_generator
# Запуск: pytest -k test_card_number_generator
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (15, 15, ["0000 0000 0000 0015"]),  # Крайнее значение (одна карта)
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),  # Максимальные значения
    ],
)
def test_card_number_generator(start: int, stop: int, expected: List[str]) -> None:
    assert list(card_number_generator(start, stop)) == expected
