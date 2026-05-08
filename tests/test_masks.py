import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        # введён корректный номер
        ("7000792289606361", "7000 79** **** 6361"),
        # номер введён с пробелами
        ("7000 7922 8960 6361", "7000  7** **** 6361"),
        # слишком короткий номер
        ("7000", "7000 ** **** 7000"),
        # слишком длинный номер
        ("7000792289606361111", "7000 79** **** 1111"),
        # пустая строка
        ("", " ** **** "),
        # введены некорректные символы
        ("word", "word ** **** word"),
    ],
)
def test_get_mask_card_number(card_number: str, expected_result: str) -> None:
    """Тестирует функцию маскировки номера карты в файле src.masks."""
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize(
    "account_number, expected_result",
    [
        # введён корректный номер
        ("73654108430135874305", "**4305"),
        # номер введён с пробелами
        ("73654 10843 01358 74305", "**4305"),
        # слишком короткий номер
        ("73654108", "**4108"),
        # слишком длинный номер
        ("736541084301358743051111", "**1111"),
        # пустая строка
        ("", "**"),
        # введены некорректные символы
        ("word", "**word"),
    ],
)
def test_get_mask_account(account_number: str, expected_result: str) -> None:
    """Тестирует функцию маскировки номера счёта в файле src.masks."""
    assert get_mask_account(account_number) == expected_result
