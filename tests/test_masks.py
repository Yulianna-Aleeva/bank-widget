import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


# Тесты для get_mask_card_number
# Запуск: pytest -k test_get_mask_card_number_parametrize
@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("70*00а79w22/89ц60-63ф61", "7000 79** **** 6361"),
        ("7000", "Номер введён неверно."),
        ("7000792289606361111", "Номер введён неверно."),
        ("Hello, World!", "Номер отсутствует."),
        ("   ", "Номер отсутствует."),
        ("", "Номер отсутствует."),
    ],
)
def test_get_mask_card_number_parametrize(card_number: str, expected_result: str) -> None:
    assert get_mask_card_number(card_number) == expected_result


# Запуск: pytest -k test_get_mask_card_number
def test_get_mask_card_number(get_mask_card_number_data: tuple) -> None:
    card_number, expected_result = get_mask_card_number_data
    assert get_mask_card_number(card_number) == expected_result


# Тесты для get_mask_account
# Запуск: pytest -k test_get_mask_account_parametrize
@pytest.mark.parametrize(
    "account_number, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("73654 10843 01358 743 05", "**4305"),
        ("в736+541,084ц301k358d743!05", "**4305"),
        ("73654108", "Номер введён неверно."),
        ("736541084301358743051111", "Номер введён неверно."),
        ("Hello, World!", "Номер отсутствует."),
        ("   ", "Номер отсутствует."),
        ("", "Номер отсутствует."),
    ],
)
def test_get_mask_account_parametrize(account_number: str, expected_result: str) -> None:
    assert get_mask_account(account_number) == expected_result


# Запуск: pytest -k test_get_mask_account
def test_get_mask_account(get_mask_account_data: tuple) -> None:
    account_number, expected_result = get_mask_account_data
    assert get_mask_account(account_number) == expected_result
