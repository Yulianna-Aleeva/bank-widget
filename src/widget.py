from datetime import datetime

from constants import DATE_FORMATS
from src.masks import get_mask_account
from src.masks import get_mask_card_number


def get_date(date_str: str) -> str:
    """Возвращает дату в формате "дд.мм.ГГГГ"."""
    if len(date_str) == 0 or date_str.isspace():
        return "Пустая строка."
    # Перебор всех возможных форматов из моего списка констант
    for format_valid in DATE_FORMATS:
        try:
            date_valid = datetime.strptime(date_str, format_valid)
            return date_valid.strftime("%d.%m.%Y")
        except ValueError:
            continue
    return "Ошибка в вводе даты."


def mask_account_card(info: str) -> str:
    """Возвращает маскированные счёт или карту."""

    if len(info) == 0:
        return "Данные отсутствуют! Строка пустая."

    if info.replace(" ", "").isalpha() or info.replace(" ", "").isdigit():
        return "Отсутствует номер или наименование карты!"

    if " " not in info:
        return "Отсутствуют пробелы между номером и названием карты или счёта!"

    name, number = info.rsplit(" ", 1)

    if name.lower().startswith("счет"):
        return f"{name} {get_mask_account(number)}"
    return f"{name} {get_mask_card_number(number)}"
