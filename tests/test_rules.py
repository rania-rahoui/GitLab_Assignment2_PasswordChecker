from password_checker.rules import check_rules
import pytest

def test_strong_password_passes_all_rules():
    result = check_rules("StrongPass1!")
    assert result == []


def test_checks_everything_but_length_password():
    result= check_rules("Short1!")
    assert result == ["Password must be at least 8 characters long"] 



def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        check_rules(12345678)
        
    with pytest.raises(TypeError):
            check_rules(None)