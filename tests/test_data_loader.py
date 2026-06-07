from pathlib import Path
from typing import Dict
from typing import List
from unittest.mock import Mock
from unittest.mock import patch

import pandas as pd
import pytest

from src.data_loader import load_transactions


@pytest.fixture(scope="module")
def csv_sample_data() -> List[Dict[str, str]]:
    """Данные из реального CSV."""
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture(scope="module")
def excel_sample_data() -> List[Dict[str, str]]:
    """Данные из реального Excel."""
    return [
        {
            "id": "632926",
            "state": "PENDING",
            "date": "2021-11-27T00:46:09Z",
            "amount": "29553",
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "American Express 6477627838877562",
            "to": "Счет 88381741644903346269",
            "description": "Перевод организации",
        },
        {
            "id": "1539387",
            "state": "EXECUTED",
            "date": "2023-07-29T18:13:23Z",
            "amount": "13130",
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": "American Express 9646246622784373",
            "to": "American Express 2760544280145973",
            "description": "Перевод с карты на карту",
        },
    ]


@patch.object(pd, "read_csv")
def test_load_csv(mock_read_csv: Mock, csv_sample_data: list[dict[str, str]], tmp_path: Path) -> None:
    """Проверяет, что CSV читается корректно."""
    mock_read_csv.return_value = pd.DataFrame(csv_sample_data)
    result = load_transactions("test.csv")
    assert result == csv_sample_data


@patch.object(pd, "read_excel")
def test_load_excel(mock_read_excel: Mock, excel_sample_data: list[dict[str, str]], tmp_path: Path) -> None:
    """Проверяет, что Excel читается корректно."""
    mock_read_excel.return_value = pd.DataFrame(excel_sample_data)
    result = load_transactions("test.xlsx")
    assert result == excel_sample_data


def test_loading_non_existing_file(tmp_path: Path) -> None:
    """Проверяет, что функция поднимает ошибку, если файла нет."""
    missing_csv = tmp_path / "nonexistent.csv"
    missing_xlsx = tmp_path / "nonexistent.xlsx"

    with pytest.raises(FileNotFoundError):
        load_transactions(str(missing_csv))

    with pytest.raises(FileNotFoundError):
        load_transactions(str(missing_xlsx))


def test_invalid_extension() -> None:
    with pytest.raises(ValueError):
        load_transactions("data.txt")
