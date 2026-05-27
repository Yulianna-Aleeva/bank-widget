from pathlib import Path
from typing import Generator

import pytest

from src.decorators import log


@pytest.fixture(autouse=True)
def cleanup_handlers() -> Generator[None, None, None]:
    """Автоматически очищает хэндлеры logging после каждого теста."""
    from src.decorators import _cleanup_handlers

    yield
    _cleanup_handlers()


def test_log_success_to_console(caplog: pytest.LogCaptureFixture) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    caplog.clear()
    add(1, 5)
    assert "add ok" in caplog.text


def test_log_success_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "success.log"

    @log(filename=str(log_file))
    def multiply(x: int, y: int) -> int:
        return x * y

    multiply(3, 4)
    content = log_file.read_text()
    assert "multiply ok" in content


def test_log_error_to_console(caplog: pytest.LogCaptureFixture) -> None:
    @log()
    def divide(a: float, b: float) -> float:
        return a / b

    caplog.clear()

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    assert "divide error: ZeroDivisionError" in caplog.text
    assert "Inputs:" in caplog.text


def test_log_error_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def fail() -> None:
        raise ValueError("Intentional failure for testing")

    with pytest.raises(ValueError):
        fail()
    content = log_file.read_text()
    assert "fail error: ValueError" in content
