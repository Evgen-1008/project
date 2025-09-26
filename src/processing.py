def filter_by_state(list_of_dicts, state='EXECUTED'):
    """
    Функция фильтрует список словарей по значению ключа 'state'.

    :param list_of_dicts: Список словарей для фильтрации
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED')
    :return: Новый список словарей, удовлетворяющих условию фильтрации
    """
    filtered_list = [item for item in list_of_dicts if item.get('state') == state]
    return filtered_list

# Пример использования
data = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'PENDING'},
    {'id': 3, 'state': 'EXECUTED'},
    {'id': 4, 'state': 'CANCELLED'}
]

filtered_data = filter_by_state(data)
print(filtered_data)
# Вывод: [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]

# Фильтрация по другому значению
filtered_data_pending = filter_by_state(data, 'PENDING')
print(filtered_data_pending)
# Вывод: [{'id': 2, 'state': 'PENDING'}]



from datetime import datetime


def sort_by_date(data_list, ascending=False):
    """
    Сортирует список словарей по дате.

    :param data_list: Список словарей, каждый из которых содержит ключ 'date'.
    :param ascending: Порядок сортировки (True - по возрастанию, False - по убыванию).
    :return: Отсортированный список словарей.
    """

    # Преобразуем даты из строк в объекты datetime для сортировки
    def get_date(item):
        return datetime.strptime(item['date'], '%Y-%m-%d')

    # Сортируем список словарей по дате
    sorted_list = sorted(data_list, key=get_date, reverse=not ascending)

    return sorted_list


# Пример использования
data = [
    {'name': 'Event A', 'date': '2024-03-11'},
    {'name': 'Event B', 'date': '2024-03-05'},
    {'name': 'Event C', 'date': '2024-03-20'}
]

# Сортировка по убыванию (по умолчанию)
sorted_data_desc = sort_by_date(data)
print("Сортировка по убыванию:", sorted_data_desc)

# Сортировка по возрастанию
sorted_data_asc = sort_by_date(data, ascending=True)
print("Сортировка по возрастанию:", sorted_data_asc)