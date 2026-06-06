import json
import logging
from typing import Dict
from typing import List
from typing import Union

# Настройка логирования для модуля src.utils
logger = logging.getLogger("src.utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions_from_json(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """Загружает транзакции из JSON-файла и возвращает пустой список при ошибке."""
    logger.info(f"Загрузка файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций.")
                return data
            else:
                logger.error("Данные в файле не являются списком.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл '{file_path}' не найден.")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле '{file_path}'. Причина: {e}")
        return []
