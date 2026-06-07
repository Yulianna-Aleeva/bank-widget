import logging

import pandas as pd

logger = logging.getLogger(__name__)


def load_transactions(file_path: str) -> list[dict]:
    """Читает транзакции из CSV или Excel."""
    logger.debug(f"Чтение файла: {file_path}")
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path, sep=";", encoding="utf-8-sig", dtype=str)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path, dtype=str)
    else:
        raise ValueError(f"Источник не поддерживается: {file_path}")
    df = df.fillna("")
    df.columns = df.columns.str.strip().str.lower()
    result = df.to_dict("records")
    logger.info(f"Прочитано {len(result)} транзакций")
    return result
