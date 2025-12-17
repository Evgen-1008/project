def mask_account_or_card(input_str: str) -> str:
    parts = input_str.strip().split()

    if parts[0].lower() == 'счет':
        # Обработка счета
        account_number = parts[-1]
        masked = '**' + account_number[-4:]
        return ' '.join(parts[:-1]) + ' ' + masked

    else:
        # Обработка карты
        card_number = parts[-1]
        masked = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
        return ' '.join(parts[:-1]) + ' ' + masked

def get_date(date_str: str) -> str:
    """
            Преобразует строку с датой в формат ДД.ММ.ГГГГ.

            :param date_str: Дата в формате "2024-03-11T02:26:18.671407"
            :return: Дата в формате "ДД.ММ.ГГГГ" (например, "11.03.2024")
            """
    date_part = date_str.split('T')[0]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"
