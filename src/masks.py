import string


def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер банковской карты."""
    clean_card_number = "".join(char for char in card_number if char in string.digits)
    if len(clean_card_number) == 0:
        return "Номер отсутствует."
    if len(clean_card_number) != 16:
        return "Номер введён неверно."
    return f"{clean_card_number[0:4]} {clean_card_number[4:6]}** **** {clean_card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер банковского счёта."""
    clean_account_number = "".join(char for char in account_number if char in string.digits)
    if len(clean_account_number) == 0:
        return "Номер отсутствует."
    if len(clean_account_number) != 20:
        return "Номер введён неверно."
    return f"**{clean_account_number[-4:]}"
