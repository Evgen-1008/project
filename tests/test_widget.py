import pytest


from src.widget import mask_account_or_card , get_date



def test_mask_account_or_card():
    # Тест для банковской карты (16 цифр)
    card_input = "Visa Platinum 7000792289606361"
    assert mask_account_or_card(card_input) == "Visa Platinum 7000 79** **** 6361"


def test_get_date():
    # Тест из примера
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"