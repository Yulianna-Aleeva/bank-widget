import requests


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли."""
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return amount

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={currency_code}&to=RUB"

    response = requests.get(url)

    from typing import TypedDict

    class ApiResponse(TypedDict):
        rates: dict[str, float]

    data: ApiResponse = response.json()

    return data["rates"]["RUB"]
