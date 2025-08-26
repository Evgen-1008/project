from typing import List


def get_mask_card_number(number_card: List[str]) -> str:
    """
    функция маскировки номера карты
    """
    number_card_1 = "".join(number_card)
    number_card_1 = number_card_1.replace(" ", "")
    mask_card = " ".join(number_card_1[i: i + 4] for i in range(0, len(number_card_1), 4))
    mask_card_list = list(mask_card)

    for i in range(len(mask_card_list)):
        if 7 <= i <= 13 and mask_card_list[i] != " ":
            mask_card_list[i] = "*"
    mask_card_number = "".join(mask_card_list)
    return mask_card_number


card_number_str = "1234567812345678"
card_number_list = list(card_number_str)
mask = get_mask_card_number(card_number_list)
print(mask)


def get_mask_account(number_cart: str) -> str:
    """Функция по маскированию номера счёта"""
    number_cart = number_cart.replace(" ", "")
    number_mask = str(number_cart[-4:])
    return f"**{number_mask}"


print(get_mask_account("123456"))