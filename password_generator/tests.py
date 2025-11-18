# tests.py
from password_module import generate_password, estimate_strength, SYMBOLS
import pytest

def test_length_and_charset():
    p = generate_password(16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)
    assert len(p) == 16

def test_no_charset_error():
    with pytest.raises(ValueError):
        generate_password(8, use_upper=False, use_lower=False, use_digits=False, use_symbols=False)

def test_invalid_length():
    with pytest.raises(ValueError):
        generate_password(0)

def test_strength_levels():
    assert estimate_strength("aaa111") == "Weak"
    assert estimate_strength("Abc123456") in ("Moderate", "Strong")
    assert estimate_strength("Abc123!@#Def") == "Strong"
