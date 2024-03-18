import json
import os
def get_data():
    """Чтение данных"""
    if os.path.isfile("data/operations.json"):
        # Код для работы в основном скрипте
        with open("data/operations.json", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Код для работы в тестах
        current_dir = os.path.dirname(__file__)
        operations_path = os.path.join(current_dir, "../data/operations.json")
        with open(operations_path, encoding="utf-8") as f:
            return json.load(f)



def filter_data(data):
    """Операции с значением ключа"""
    filter_operations = [operation for operation in data if "state" in operation and operation["state"] == "EXECUTED"]
    return filter_operations

def last_five_operations(data):
    """Сортировка и вывод последних 5 операций"""
    sorted_operations = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_operations[:5]

def format_date(date: str):
    """Возвращение строки даты"""
    date_format = date.split("T")[0].split("-")[::-1]
    return ".".join(date_format)

def format_card(card: str):
    """Скрытие номера счета"""
    card = card.split()
    card_number = card.pop()
    card_name = " ".join(card)
    if card_name.lower() == "счет":
        number_secret = "**" + card_number[-4:]
    else:
        number_secret = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_name} {number_secret}"

def get_data_format(data):
    operations = []
    for operation in data:
        date = format_date(operation["date"])
        if "from" in operation:
            from_formatted = format_card(operation["from"])
        else:
            from_formatted = ""

        to_formatted = format_card(operation["to"])
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]
        date_formatted = format_date(operation["date"])
        description = operation["description"]
        formatted_operation = f"{date_formatted} {description}\n{from_formatted} -> {to_formatted}\n{amount} {currency}\n"
        operations.append(formatted_operation)

    return operations

