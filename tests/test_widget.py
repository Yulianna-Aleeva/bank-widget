from src.widget import get_date
from src.widget import mask_account_card


# Запуск: pytest -k test_get_date
def test_get_date(get_date_data: tuple) -> None:
    date_str, expected_result = get_date_data
    assert get_date(date_str) == expected_result


# Запуск: pytest -k mask_account_card
def test_mask_account_card(mask_account_card_data: tuple) -> None:
    bank_number, expected_result = mask_account_card_data
    assert mask_account_card(bank_number) == expected_result
