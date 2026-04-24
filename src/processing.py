from typing import Any
from typing import Dict
from typing import List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Возвращает новый список словарей, соответствующий указанному значению "state"."""
    return [item for item in operations if item.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Возвращает список, отсортированный по дате."""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
