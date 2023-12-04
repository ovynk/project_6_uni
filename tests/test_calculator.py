from app.calculator import Calculator
from pytest import raises


calculator = Calculator(3, 13.1)
calculator_zero = Calculator(-3.1, 0)


def test_plus():
    expected_data = 16.1
    actual_data = calculator.plus()

    assert expected_data == actual_data


def test_zero_plus():
    expected_data = -3.1
    actual_data = calculator_zero.plus()

    assert expected_data == actual_data


def test_minus():
    expected_data = -10.1
    actual_data = calculator.minus()

    assert expected_data == actual_data


def test_zero_minus():
    expected_data = -3.1
    actual_data = calculator_zero.minus()

    assert expected_data == actual_data


def test_divide():
    expected_data = 0.22900763358778625
    actual_data = calculator.divide()

    assert expected_data == actual_data


def test_invalid_divide():
    with raises(ZeroDivisionError):
        calculator_zero.divide()


def test_multiply():
    expected_data = 39.3
    actual_data = calculator.multiply()

    assert expected_data == actual_data


def test_zero_multiply():
    expected_data = 0.0
    actual_data = calculator_zero.multiply()

    assert isinstance(actual_data, float)
    assert expected_data == actual_data


def test_pow():
    expected_data = 1779460.847195256
    actual_data = calculator.pow()

    assert expected_data == actual_data


def test_zero_pow():
    expected_data = 1
    actual_data = calculator_zero.pow()

    assert expected_data == actual_data


def test_valid_random():
    actual_data = calculator.random(10, 12)

    assert 10 <= actual_data <= 12


def test_invalid_random():
    with raises(ValueError):
        Calculator.random(9, 9)
