from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from src.data_loader import load_transactions

OperationsList = List[Dict[str, Any]]


def _validate_data(data: OperationsList, expected: OperationsList) -> None:
    assert len(data) == len(expected)

    for i, (row, expected_row) in enumerate(zip(data, expected)):
        flat_fields = ["id", "state", "date", "from", "to", "description"]
        for field in flat_fields:
            assert row.get(field) == expected_row.get(field), f"Не совпадают значения в поле '{field}' строки {i}"
        op_amount = row.get("operationAmount", {})
        exp_op_amount = expected_row.get("operationAmount", {})
        assert op_amount.get("amount") == exp_op_amount.get("amount"), f"Не совпадают суммы в строке {i}"
        currency = op_amount.get("currency", {})
        exp_currency = exp_op_amount.get("currency", {})
        assert currency.get("name") == exp_currency.get("name"), f"Не совпадают названия валют в строке {i}"
        assert currency.get("code") == exp_currency.get("code"), f"Не совпадают коды валют в строке {i}"


def test_load_csv(csv_file_path: str, test_data: OperationsList) -> None:
    result = load_transactions(str(csv_file_path))
    expected_data = []
    for row in test_data:
        new_row = {k: v for k, v in row.items() if k not in ["amount", "currency_name", "currency_code"]}
        new_row["operationAmount"] = {
            "amount": row.get("amount", ""),
            "currency": {"name": row.get("currency_name", ""), "code": row.get("currency_code", "")},
        }
        expected_data.append(new_row)
    _validate_data(result, expected_data)


def test_load_json(json_file_path: str, test_data: OperationsList) -> None:
    result = load_transactions(str(json_file_path))
    expected_data = []
    for row in test_data:
        new_row = {k: v for k, v in row.items() if k not in ["amount", "currency_name", "currency_code"]}
        new_row["operationAmount"] = {
            "amount": row.get("amount", ""),
            "currency": {"name": row.get("currency_name", ""), "code": row.get("currency_code", "")},
        }
        expected_data.append(new_row)
    _validate_data(result, expected_data)


def test_load_excel(excel_file_path: str, test_data: OperationsList) -> None:
    result = load_transactions(str(excel_file_path))
    expected_data = []
    for row in test_data:
        new_row = {k: v for k, v in row.items() if k not in ["amount", "currency_name", "currency_code"]}
        new_row["operationAmount"] = {
            "amount": row.get("amount", ""),
            "currency": {"name": row.get("currency_name", ""), "code": row.get("currency_code", "")},
        }
        expected_data.append(new_row)
    _validate_data(result, expected_data)


# Тесты на обработку ошибок
def test_empty_excel(tmp_path: Path) -> None:
    empty_excel_path = tmp_path / "empty.xlsx"
    pd.DataFrame({}).to_excel(empty_excel_path, index=False)
    result = load_transactions(str(empty_excel_path))
    assert result == []


def test_corrupted_excel(tmp_path: Path) -> None:
    corrupted_excel_path = tmp_path / "corrupted.xlsx"
    with open(corrupted_excel_path, "w") as f:
        f.write("Это не Excel файл")
    result = load_transactions(str(corrupted_excel_path))
    assert result == []


def test_invalid_excel_structure(tmp_path: Path) -> None:
    invalid_excel_path = tmp_path / "invalid_structure.xlsx"
    pd.DataFrame({"wrong_column": ["1", "2", "3"]}).to_excel(invalid_excel_path, index=False)
    result = load_transactions(str(invalid_excel_path))
    assert len(result) == 3
    assert result[0].get("wrong_column") == "1"
    assert "operationAmount" in result[0]


def test_large_numbers_in_excel(tmp_path: Path) -> None:
    raw_data = [
        {"id": "99999999999999999999", "amount": "99999999999999999999"},
        {"id": "1", "amount": "1"},
    ]
    large_excel_path = tmp_path / "large_numbers.xlsx"
    pd.DataFrame(raw_data).to_excel(large_excel_path, index=False)
    expected_data = [
        {
            "id": "99999999999999999999",
            "amount": "99999999999999999999",
            "operationAmount": {"amount": "99999999999999999999", "currency": {"name": "", "code": ""}},
        },
        {
            "id": "1",
            "amount": "1",
            "operationAmount": {"amount": "1", "currency": {"name": "", "code": ""}},
        },
    ]
    result = load_transactions(str(large_excel_path))
    assert result == expected_data


def test_missing_columns_excel(tmp_path: Path) -> None:
    partial_data = [{"id": "1", "state": "EXECUTED", "date": "2023-01-01"}]
    partial_excel_path = tmp_path / "partial_columns.xlsx"
    pd.DataFrame(partial_data).to_excel(partial_excel_path, index=False)
    result = load_transactions(str(partial_excel_path))
    assert len(result) == 1
    assert result[0]["id"] == "1"
    op_amount = result[0].get("operationAmount", {})
    assert op_amount.get("amount") == ""
