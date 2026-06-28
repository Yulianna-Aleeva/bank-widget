import json
import logging
from typing import Any, Dict, List

import pandas as pd

logger = logging.getLogger("src.data_loader")

OperationsList = List[Dict[str, Any]]


def _json_object_hook(dct: Dict[Any, Any]) -> Dict[str, Any]:
    """Преобразует все числовые значения в словаре в строки."""
    return {str(k): (str(v) if isinstance(v, (int, float)) else v) for k, v in dct.items()}


def _normalize_row(row: Dict[str, Any]) -> Dict[str, Any]:
    """
    Приводит одну запись к единому формату.
    Args:
        row (Dict[str, Any]): Строка данных из файла (JSON/CSV/Excel).
    Returns:
        Dict[str, Any]: Словарь, приведенный к стандартному формату.
    """
    row = {str(k): v for k, v in row.items()}

    return {
        **row,
        "operationAmount": row.get(
            "operationAmount",
            {
                "amount": row.get("amount", ""),
                "currency": {"name": row.get("currency_name", ""), "code": row.get("currency_code", "")},
            },
        ),
    }


def load_transactions(file_path: str) -> OperationsList:
    logger.info(f"Загрузка файла: {file_path}")

    try:
        if file_path.lower().endswith(".json"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f, object_hook=_json_object_hook)

                    if isinstance(data, list):
                        return [_normalize_row(row) for row in data]
                    elif isinstance(data, dict):
                        return [_normalize_row(data)]
                    else:
                        logger.error(f"Неожиданный формат данных в JSON-файле: {type(data)}.")
                        return []
            except (FileNotFoundError, json.JSONDecodeError) as e:
                logger.error(f"Ошибка при чтении JSON-файла '{file_path}': {e}.")
                return []

        elif file_path.lower().endswith(".csv"):
            try:
                df = pd.read_csv(file_path, sep=None, dtype=str, encoding="utf-8", engine="python", quoting=3)
                df = df.fillna("")

                required_columns = {
                    "id",
                    "state",
                    "date",
                    "amount",
                    "currency_name",
                    "currency_code",
                    "from",
                    "to",
                    "description",
                }
                actual_columns_lower = {col.strip().lower() for col in df.columns}

                if not required_columns.issubset(actual_columns_lower):
                    missing_cols = required_columns - actual_columns_lower
                    logger.error(f"Отсутствуют обязательные столбцы в CSV-файле: {missing_cols}.")
                    return []

                raw_data = [
                    {str(k): v.strip() if isinstance(v, str) else v for k, v in row.items()}
                    for row in df.to_dict(orient="records")
                ]

                return [_normalize_row(row) for row in raw_data]

            except Exception as e:
                logger.error(f"Ошибка при чтении CSV-файла '{file_path}': {e}.")
                return []

        else:
            try:
                df = pd.read_excel(file_path, dtype=str, engine="openpyxl")
                df = df.fillna("")
                raw_data = [
                    {str(k): v.strip() if isinstance(v, str) else v for k, v in row.items()}
                    for row in df.to_dict(orient="records")
                ]
                return [_normalize_row(row) for row in raw_data]
            except Exception as e:
                logger.error(f"Ошибка при чтении Excel-файла '{file_path}': {e}.")
                return []

    except FileNotFoundError as e:
        logger.error(f"Файл '{file_path}' не найден: {e}.")
        return []
    except Exception as e:
        logger.error(f"Критическая ошибка при чтении файла '{file_path}': {e}.")
        return []
