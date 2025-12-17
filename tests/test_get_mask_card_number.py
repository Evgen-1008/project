from src.masks import get_mask_card_number


def test_get_mask_cart_number():
    assert get_mask_card_number("7556 7748 8893 8885") == "7556 77** **** 8885"
