from src.masks import get_mask_account
from src.masks import get_mask_card_number

if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_card_number("7000 7922 8960 6361"))
    print(get_mask_card_number("7000а7922/8960-6361"))
    print(get_mask_card_number("7000"))
    print(get_mask_card_number("7000792289606361111"))
    print(get_mask_card_number("Hello, World!"))
    print(get_mask_card_number("  "))
    print(get_mask_card_number(""))
    # print(get_mask_card_number(""))

if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
    print(get_mask_account("73654 10843 01358 743 05"))
    print(get_mask_account("в736+541,084ц301k358d743!05"))
    print(get_mask_account("73654108"))
    print(get_mask_account("736541084301358743051111"))
    print(get_mask_account("Hello, World!"))
    print(get_mask_account("   "))
    print(get_mask_account(""))
    # print(get_mask_account(""))
