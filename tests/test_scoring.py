
import pytest
from password_checker.scoring import check_strength


def test_strong_password():
    assert check_strength("Hello123!") == (5, "Strong")


def test_short_password():
    assert check_strength("Hi1!") == (4, "Medium")


def test_invalid_password():
    with pytest.raises(TypeError):
        check_strength(None)

def test_weak_password():
    assert check_strength("abc") == (1, "Weak")