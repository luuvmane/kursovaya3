from src.utils import get_data, filter_data, last_five_operations, get_data_format

"""Получение данных из файла"""
data = get_data()

"""Фильтрация данных, выбор последних пяти операций и форматирование"""
filtered_data = filter_data(data)
last_five = last_five_operations(filtered_data)
formatted_operations = get_data_format(last_five)

"""Вывод отформатированных операций"""
for operation in formatted_operations:
    print(operation)
