import pytest


def calculate_bonus(years_worked: float, stick: bool):
    if years_worked >= 3:
        bonus = 30
    elif 1.5 <= years_worked < 3:
        bonus = 25
    elif 0.25 <= years_worked < 1.5:
        bonus = 15
    else:
        return 0

    if stick:
        pass
    else:
        bonus += 3

    return bonus


@pytest.mark.parametrize("years_worked, stick, expected_bonus", [
    (4, False, 33),
    (2, False, 28),
    (1, False, 18),
    (0.5, True, 15),
    (3, True, 30),
    (0.1, False, 0),
    (0.25, False, 18),
    (0, True, 0),
    (10, True, 30),
])
def test_calculate_bonus(years_worked, stick, expected_bonus):
    assert calculate_bonus(years_worked, stick) == expected_bonus

