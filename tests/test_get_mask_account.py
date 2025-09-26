from src.masks import get_mask_account


def test_get_mask_account():
    assert get_mask_account("4544565336675446") == "**5446"