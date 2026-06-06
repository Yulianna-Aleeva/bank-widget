import logging
import string

logger = logging.getLogger("src.masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s: %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер банковской карты."""
    logger.info(f"Маскировка карты: {card_number}")

    clean_card_number = "".join(char for char in card_number if char in string.digits)

    if not clean_card_number or clean_card_number.isspace():
        logger.error("Данные не содержат цифр.")
        return "Номер отсутствует."

    if len(clean_card_number) != 16:
        logger.error(f"Неверная длина номера карты: {len(clean_card_number)}. Ожидаемая длина = 16.")
        return "Номер введён неверно."

    masked = f"{clean_card_number[0:4]} {clean_card_number[4:6]}** **** {clean_card_number[-4:]}"
    logger.debug(f"Результат: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер банковского счёта."""
    logger.info(f"Маскировка счёта: {account_number}")

    clean_account_number = "".join(char for char in account_number if char in string.digits)

    if not clean_account_number or clean_account_number.isspace():
        logger.error("Данные не содержат цифр.")
        return "Номер отсутствует."

    if len(clean_account_number) != 20:
        logger.error(f"Неверная длина номера счёта: {len(clean_account_number)}. Ожидаемая длина = 20.")
        return "Номер введён неверно."

    masked = f"**{clean_account_number[-4:]}"
    logger.debug(f"Результат: {masked}")
    return masked
