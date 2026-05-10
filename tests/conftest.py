import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import get_date
from src.widget import mask_account_card

# Расположение: src.masks.py
TEST_GET_MASK_CARD_NUMBER_DATA = [
    "7000792289606361",
    "7000 7922 8960 6361",
    "70*00а79w22/89ц60-63ф61",
    "7000",
    "7000792289606361111",
    "Hello, World!",
    "   ",
    "",
]


@pytest.fixture(params=TEST_GET_MASK_CARD_NUMBER_DATA)
def mask_card_data(request: pytest.FixtureRequest) -> tuple:
    input_data = request.param
    expected = get_mask_card_number(input_data)
    return input_data, expected


# Расположение: src.masks.py
TEST_GET_MASK_ACCOUNT_DATA = [
    "73654108430135874305",
    "73654 10843 01358 743 05",
    "в736+541,084ц301k358d743!05",
    "73654108",
    "736541084301358743051111",
    "Hello, World!",
    "   ",
    "",
]


@pytest.fixture(params=TEST_GET_MASK_ACCOUNT_DATA)
def mask_account_data(request: pytest.FixtureRequest) -> tuple:
    input_data = request.param
    expected = get_mask_account(input_data)
    return input_data, expected


# Расположение: src.widget.py
TEST_GET_DATE_DATA = [
    "2008-03-03T17:20:01.051988",
    "2008-03-03T17:20:01",
    "2008-03-03",
    "2008-3-3",
    "08-3-3",
    "20080303",
    "2008d03f03",
    "8-3-3",
    "3.3.8",
    "3/3/8",
    "32-13-2026",
    "2026.15.01",
    "2026/01-01",
    "2026-01.01",
    "Hello, World!",
    "   ",
    "",
]


@pytest.fixture(params=TEST_GET_DATE_DATA)
def get_date_data(request: pytest.FixtureRequest) -> tuple:
    input_data = request.param
    expected = get_date(input_data)
    return input_data, expected


# Расположение: src.widget.py
TEST_MASK_ACCOUNT_CARD_DATA = [
    "Visa Platinum 7000792289606361",
    "Счет 73654108430135874305",
    "VisaPlatinum7000792289606361",
    "Счет 73654108430135874305",
    "Visa 7000792289606361",
    "Счет 73654dg108fg430fh135dfg874fg305",
    " Platinum 7000792289606361 ",
    "С ч е т 7 3 6 5 4 1 0 8 4 3 0 1 3 5 8 7 4 3 0 5",
    "V i s a P l a t i n u m 7000792289606361",
    "1156623212313153212",
    "7000792289606361",
    "CСч1ёт 1234",
    "VisaPlatinum",
    "Счёт",
    "Счёт     1234" "Карта банка" "С1ч2е3т4",
    "Счёт123 456...",
    ",Счета " " ! ",
    "WOW 357951",
    "Hello, World!",
    "   ",
    "",
]


@pytest.fixture(params=TEST_MASK_ACCOUNT_CARD_DATA)
def mask_account_card_data(request: pytest.FixtureRequest) -> tuple:
    input_data = request.param
    expected = mask_account_card(input_data)
    return input_data, expected
