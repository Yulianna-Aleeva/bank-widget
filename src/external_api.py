from typing import TypedDict

import requests


class ApiResponse(TypedDict):
    result: float


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли."""
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"

    headers = {"apikey": "hSduqg7Z128RUH3eYgwCajeYlrYx43JS"}

    response = requests.get(url, headers=headers)  # type: ignore
    data: ApiResponse = response.json()  # Используем аннотацию для ответа

    return data["result"]


# Мой бесплатный вариант без регистрации и блокировок
# import requests
# def convert_to_rub(transaction: dict) -> float:
#     """Конвертирует сумму транзакции в рубли."""
#     amount = float(transaction["operationAmount"]["amount"])
#     currency_code = transaction["operationAmount"]["currency"]["code"]
#     if currency_code == "RUB":
#         return amount
#     url = f"https://api.frankfurter.app/latest?amount={amount}&from={currency_code}&to=RUB"
#     response = requests.get(url)
#     from typing import TypedDict
#     class ApiResponse(TypedDict):
#         rates: dict[str, float]
#     data: ApiResponse = response.json()
#     return data["rates"]["RUB"]
