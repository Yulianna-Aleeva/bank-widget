from pathlib import Path
from unittest.mock import Mock
from unittest.mock import patch

from src.external_api import convert_to_rub
from src.utils import load_transactions_from_json


def test_load_transactions_success(tmp_path: Path) -> None:
    file = tmp_path / "test.json"
    file.write_text('[{"id": 1}]')
    assert load_transactions_from_json(str(file)) == [{"id": 1}]


def test_load_file_not_found() -> None:
    assert load_transactions_from_json("no_file.json") == []


def test_load_invalid_json(tmp_path: Path) -> None:
    file = tmp_path / "invalid.json"
    file.write_text('{"broken": [}')
    assert load_transactions_from_json(str(file)) == []


def test_load_not_a_list(tmp_path: Path) -> None:
    file = tmp_path / "not_a_list.json"
    file.write_text('{"key": "value"}')
    result = load_transactions_from_json(str(file))
    assert result == []


@patch("src.external_api.requests.get")
def test_convert_to_rub_already_rub(mock_get: Mock) -> None:
    transaction = {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}}
    assert convert_to_rub(transaction) == 500.0
    mock_get.assert_not_called()


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get: Mock) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 9000.0}}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    assert convert_to_rub(transaction) == 9000.0
    mock_get.assert_called_once()
