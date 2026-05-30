import json
from typing import Dict
from typing import List
from typing import Union


def load_transactions_from_json(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """Загружает транзакции из JSON-файла и возвращает пустой список при ошибке."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("Данные в файле не являются списком. Возвращается пустой список.")
                return []
    except FileNotFoundError:
        print(f"Файл {file_path} не найден. Возвращается пустой список.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {file_path}. Файл пустой или повреждённый.")
        return []
