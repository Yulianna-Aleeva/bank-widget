import atexit
import logging
from functools import wraps
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional

# Словарь для хранения созданных обработчиков
_handlers: Dict[Optional[str], Any] = {}


def _cleanup_handlers() -> None:
    """Функция для закрытия всех открытых обработчиков при выходе из программы."""
    for handler in _handlers.values():
        handler.close()


atexit.register(_cleanup_handlers)


def log(filename: Optional[str] = None) -> Callable[..., Any]:
    """Декоратор для логирования вызова функции."""
    if filename not in _handlers:
        if filename:
            handler = logging.FileHandler(filename, encoding="utf-8")
        else:
            handler = logging.StreamHandler()  # type: ignore
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        _handlers[filename] = handler

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        logger_name = f"decorator.{func.__name__}"
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            logger.addHandler(_handlers[filename])

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: args={args}, kwargs={kwargs}")
                raise

        return wrapper

    return decorator
