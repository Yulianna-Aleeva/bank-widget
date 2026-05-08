# import datetime
# import string

import pytest

from src.widget import get_date

# from src.widget import mask_account_card


@pytest.mark.parametrize(
    "date_str, expected_result",
    [
        # введена корректная дата
        ("2008-03-03T17:20:01.051988", "03.03.2008"),
        ("2008-03-03T17:20:01", "03.03.2008"),
        ("2008-03-03", "03.03.2008"),
        ("2008-3-3", "03.03.2008"),
        ("08-3-3", "03.03.2008"),
        ("20080303", "03.03.2008"),
        # короткий формат даты
        ("8-3-3", "Ошибка в вводе даты."),
        ("3.3.8", "Ошибка в вводе даты."),
        ("3/3/8", "Ошибка в вводе даты."),
        # пустой ввод
    ],
)
def test_get_date(date_str: str, expected_result: str) -> None:
    """Тестирует функцию корректировки даты в файле src.widget."""
    assert get_date(date_str) == expected_result


# В РАБОТЕ
# @pytest.mark.parametrize(
#     "info, expected_result",
#     [
#         #
#         ("", ""),
#         #
#         ("", ""),
#     ],
# )
# def test_mask_account_card(info: str, expected_result: str) -> None:
#     """Тестирует функцию маскировки номера счёта и карты в файле src.widget."""
#     assert mask_account_card(info) == expected_result
