from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import get_date
from src.widget import mask_account_card

if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_card_number("7000 7922 8960 6361"))
    print(get_mask_card_number("7000"))
    print(get_mask_card_number("7000792289606361111"))
    print(get_mask_card_number(""))
    print(get_mask_card_number("word"))
    # print(get_mask_card_number(""))

if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
    print(get_mask_account("73654 10843 01358 74305"))
    print(get_mask_account("73654108"))
    print(get_mask_account("736541084301358743051111"))
    print(get_mask_account(""))
    # print(get_mask_account(""))

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Visa Platinum 7000 79228 9606 361"))
    print(mask_account_card("Счет 7365 41084 3013 5874305"))
    print(mask_account_card("Visa Platinum 7000"))
    print(mask_account_card("Счет 7365"))
    print(mask_account_card("Visa Platinum 7000792289606361111"))
    print(mask_account_card("Счет 73654108430135874305111"))
    print(mask_account_card("  "))
    print(mask_account_card(" "))
    print(mask_account_card(""))
    print(mask_account_card("VisaPlatinum7000792289606361"))
    print(mask_account_card("Счет73654108430135874305"))
    print(mask_account_card("7000792289606361"))
    print(mask_account_card("73654108430135874305"))
    print(mask_account_card("Visa Platinum"))
    print(mask_account_card("Счет"))
    # print(mask_account_card(""))

if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
    print(get_date("2024 03 11 02 26 18 671407"))
    print(get_date("2024-03-11T02:26:18"))
    print(get_date("11.03.2024"))
    print(get_date("02:26:18"))
    print(get_date("02:26:18.671407"))
    print(get_date("2024-03-11T02:26:18.671407111"))
    print(get_date(""))
    print(get_date("word"))
    # print(get_date(""))
