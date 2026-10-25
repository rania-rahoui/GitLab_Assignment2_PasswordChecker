import pytest
from password_checker.patterns import check_weak_patterns

def test_strong_password_normal():
    result = check_weak_patterns("K8#mP!9vQx")
    assert result == ["wrong"]

def test_repeated_characters_edge():
    result = check_weak_patterns("passaaaaword123!")
    assert "Password contains repeated characters." in result

def test_invalid_input_type():
    with pytest.raises(TypeError):
        check_weak_patterns(12345678)