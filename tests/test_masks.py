from src.masks import get_mask_account
from src.masks import get_mask_card_number


# Запуск: pytest -k test_get_mask_card_number
def test_get_mask_card_number(mask_card_data: tuple) -> None:
    card_number, expected_result = mask_card_data
    assert get_mask_card_number(card_number) == expected_result


# Запуск: pytest -k test_get_mask_account
def test_get_mask_account(mask_account_data: tuple) -> None:
    account_number, expected_result = mask_account_data
    assert get_mask_account(account_number) == expected_result
