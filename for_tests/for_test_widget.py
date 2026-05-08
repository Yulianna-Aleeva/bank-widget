from src.widget import get_date

# from src.widget import mask_account_card

if __name__ == "__main__":
    print(get_date("2008-03-03T17:20:01.051988"))
    print(get_date("2008-03-03T17:20:01"))
    print(get_date("2008-03-03"))
    print(get_date("2008-3-3"))
    print(get_date("08-3-3"))
    print(get_date("20080303"))
    print(get_date("8-3-3"))
    print(get_date("3.3.8"))
    print(get_date("3/3/8"))
    print(get_date(""))
    print(get_date(""))
    print(get_date(""))
    print(get_date(""))
    print(get_date(""))
    print(get_date(""))
    print(get_date(""))


# if __name__ == "__main__":
# print(mask_account_card(""))
