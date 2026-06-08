import logging

import pandas as pd

logger = logging.getLogger(__name__)


def load_transactions(file_path: str) -> list[dict]:
    """Читает транзакции из CSV или Excel."""
    logger.debug(f"Чтение файла: {file_path}")
    lower_file_path = file_path.lower()
    if lower_file_path.endswith(".csv"):
        df = pd.read_csv(file_path, sep=";", encoding="utf-8-sig", dtype=str)
    elif lower_file_path.endswith((".xlsx", ".xls")):
        df = pd.read_excel(file_path, dtype=str)
    else:
        raise ValueError(f"Формат файла не поддерживается: {file_path}")
    df.replace("", pd.NA, inplace=True)
    result = df.to_dict("records")
    logger.info(f"Прочитано {len(result)} транзакций")
    return result
