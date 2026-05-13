import pytest

from src.widget import get_date
from src.widget import mask_account_card


# Тесты для get_date
# Запуск: pytest -k test_get_date_parametrize
@pytest.mark.parametrize(
    "date_str, expected_result",
    [
        ("2008-03-03T17:20:01.051988", "03.03.2008"),
        ("2008-03-03T17:20:01", "03.03.2008"),
        ("2008-03-03", "03.03.2008"),
        ("2008-3-3", "03.03.2008"),
        ("08-3-3", "03.03.2008"),
        ("20080303", "03.03.2008"),
        ("2008d03f03", "Ошибка в вводе даты."),
        ("8-3-3", "Ошибка в вводе даты."),
        ("3.3.8", "Ошибка в вводе даты."),
        ("3/3/8", "Ошибка в вводе даты."),
        ("32-13-2026", "Ошибка в вводе даты."),
        ("2026.15.01", "Ошибка в вводе даты."),
        ("2026/01-01", "Ошибка в вводе даты."),
        ("2026-01.01", "Ошибка в вводе даты."),
        ("Hello, World!", "Ошибка в вводе даты."),
        ("   ", "Пустая строка."),
        ("", "Пустая строка."),
    ],
)
def test_get_date_parametrize(date_str: str, expected_result: str) -> None:
    assert get_date(date_str) == expected_result


# Запуск: pytest -k test_get_date
def test_get_date(get_date_data: tuple) -> None:
    date_str, expected_result = get_date_data
    assert get_date(date_str) == expected_result


# Тесты для mask_account_card
# Запуск: pytest -k test_mask_account_card_parametrize
@pytest.mark.parametrize(
    "bank_number, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("VisaPlatinum7000792289606361", "Отсутствуют пробелы между номером и счетом."),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),
        ("Счет 73654dg108fg430fh135dfg874fg305", "Счет **4305"),
        (" Platinum 7000792289606361 ", "Отсутствуют пробелы между номером и счетом."),
        (
            "С ч е т 7 3 6 5 4 1 0 8 4 3 0 1 3 5 8 7 4 3 0 5",
            "С ч е т 7 3 6 5 4 1 0 8 4 3 0 1 3 5 8 7 4 3 0 Номер введён неверно.",
        ),
        ("V i s a P l a t i n u m 7000792289606361", "V i s a P l a t i n u m 7000 79** **** 6361"),
        ("1156623212313153212", "Отсутствуют пробелы между номером и счетом."),
        ("7000792289606361", "Отсутствуют пробелы между номером и счетом."),
        ("CСч1ёт 1234", "CСч1ёт Номер введён неверно."),
        ("VisaPlatinum", "Отсутствуют пробелы между номером и счетом."),
        ("Счёт", "Отсутствуют пробелы между номером и счетом."),
        ("Счёт     1234Карта банкаС1ч2е3т4", "Счёт     1234Карта Номер введён неверно."),
        ("Счёт123 456...", "Счёт123 Номер введён неверно."),
        (",Счета  ! ", "Отсутствуют пробелы между номером и счетом."),
        ("WOW 357951", "WOW Номер введён неверно."),
        ("Hello, World!", "Hello, Номер отсутствует."),
        ("   ", "Данные отсутствуют."),
        ("", "Данные отсутствуют."),
    ],
)
def test_mask_account_card_parametrize(bank_number: str, expected_result: str) -> None:
    assert mask_account_card(bank_number) == expected_result


# Запуск: pytest -k test_mask_account_card
def test_mask_account_card(mask_account_card_data: tuple) -> None:
    bank_number, expected_result = mask_account_card_data
    assert mask_account_card(bank_number) == expected_result
