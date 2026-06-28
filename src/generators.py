from typing import Any, Dict, Iterator, List

OperationsList = List[Dict[str, Any]]


def filter_by_currency(transactions: OperationsList, currency: str) -> OperationsList:
    """Фильтрует транзакции по заданной валюте и возвращает список."""
    return [
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
    ]
    # yield transaction


def transaction_descriptions(transactions: OperationsList) -> Iterator[str]:
    """Генератор описаний транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        yield " ".join([card_str[i : i + 4] for i in range(0, 16, 4)])  # noqa: E203
