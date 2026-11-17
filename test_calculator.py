import pytest

from calculator import Calculator


@pytest.mark.parametrize("left,right,expected", [(2, 3, 5), (-3, 3, 0), (0, 0, 0), (0.2, 0.3, 0.5)])
def test_add(left, right, expected):
    assert Calculator.add(left, right) == pytest.approx(expected)


@pytest.mark.parametrize("left,right,expected", [(5, 2, 3), (2, 5, -3), (0, 0, 0), (-2, -3, 1)])
def test_subtract(left, right, expected):
    assert Calculator.subtract(left, right) == expected


@pytest.mark.parametrize("left,right,expected", [(4, 3, 12), (-3, 4, -12), (0, 8, 0), (1.5, 2, 3)])
def test_multiply(left, right, expected):
    assert Calculator.multiply(left, right) == pytest.approx(expected)


@pytest.mark.parametrize("left,right,expected", [(8, 2, 4), (-8, 2, -4), (0, 3, 0), (1, 3, 1 / 3)])
def test_divide(left, right, expected):
    assert Calculator.divide(left, right) == pytest.approx(expected)


@pytest.mark.parametrize("left,right", [(1, 0), (0, 0), (-5, -0.0)])
def test_divide_by_zero(left, right):
    with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
        Calculator.divide(left, right)


@pytest.mark.parametrize("number,expected", [(-7, False), (0, False), (1, False), (2, True), (3, True), (4, False), (49, False), (97, True)])
def test_is_prime_number(number, expected):
    assert Calculator.is_prime_number(number) is expected


@pytest.mark.parametrize("value", [3.0, "3", True])
def test_is_prime_number_rejects_non_integer(value):
    with pytest.raises(TypeError, match="Ожидается целое число"):
        Calculator.is_prime_number(value)
