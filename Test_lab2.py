import Lab2

def test_calc_average():
    numbers = [10, 20, 30, 40]
    result = Lab2.calc_average(numbers)
    assert result == 25  # (10+20+30+40)/4 = 25

def test_find_min_max():
    numbers = [30.5, 32.0, 28.7, 31.2]
    result = Lab2.find_min_max(numbers)
    assert result == [28.7, 32.0]

def test_calc_median_temperature_odd():
    temperatures = [30.5, 32.0, 28.7]  # sorted → [28.7, 30.5, 32.0]
    result = Lab2.calc_median_temperature(temperatures)
    assert result == 30.5

def test_calc_median_temperature_even():
    temperatures = [30.5, 32.0, 28.7, 31.2]  # sorted → [28.7, 30.5, 31.2, 32.0]
    result = Lab2.calc_median_temperature(temperatures)
    expected = (30.5 + 31.2) / 2  # = 30.85
    assert result == expected
