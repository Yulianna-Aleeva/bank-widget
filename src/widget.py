from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Возвращает маскированные счёт или карту."""

    name, number = info.rsplit(" ", 1)

    if name.lower().startswith("счет"):
        return f"{name} {get_mask_account(number)}"
    return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Возвращает преобразованную дату."""

    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[0:4]}"
