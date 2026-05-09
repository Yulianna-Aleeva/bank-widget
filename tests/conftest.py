import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


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
def card_data(request):
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
def account_data(request):
    input_data = request.param
    expected = get_mask_account(input_data)
    return input_data, expected