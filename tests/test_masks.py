from src.masks import get_mask_card_number
from src.masks import get_mask_account


# Запуск: pytest -k test_get_mask_card_number
def test_get_mask_card_number(card_data):
    card_number, expected_result = card_data
    assert get_mask_card_number(card_number) == expected_result


# Запуск: pytest -k test_get_mask_account
def test_get_mask_account(account_data):
    account_number, expected_result = account_data
    assert get_mask_account(account_number) == expected_result