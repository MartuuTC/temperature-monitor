from temperature import celsius_to_fahrenheit, is_fever


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(25) == 77
    assert celsius_to_fahrenheit(100) == 212


def test_is_fever():
    assert is_fever(36) == False
    assert is_fever(37.5) == False
    assert is_fever(38) == True
    assert is_fever(39) == True
