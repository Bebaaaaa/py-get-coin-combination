import pytest
from app.main import get_coin_combination

def test_return_only_pennies():
    result = get_coin_combination(3)
    assert result == [3, 0, 0, 0]
    result2 = get_coin_combination(41)
    assert sum(1 for c in result2 if c > 0) > 1


@pytest.mark.parametrize(
    "cents, coin_index",
    [
        (1, 0),   
        (5, 1),   
        (10, 2),  
        (25, 3),  
    ],
)
def test_return_only_one_type(cents, coin_index):
    result = get_coin_combination(cents)
    non_zero_types = sum(1 for c in result if c > 0)
    assert non_zero_types == 1
    assert result[coin_index] > 0


def test_return_multiple_types():
    result = get_coin_combination(41)
    non_zero = sum(1 for c in result if c > 0)
    assert non_zero > 1