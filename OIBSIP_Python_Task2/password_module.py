import string
import secrets

SYMBOLS = "!@#$%&*()-_=+[]{};:,.<>?"

def generate_password(length: int = 12,
                      use_upper: bool = True,
                      use_lower: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = True) -> str:
    if length <= 0:
        raise ValueError("length must be positive")

    charset = ""
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += SYMBOLS

    if not charset:
        raise ValueError("At least one character set must be enabled")

    return ''.join(secrets.choice(charset) for _ in range(length))


def estimate_strength(password: str) -> str:
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in SYMBOLS for c in password): score += 1
    if len(password) >= 12: score += 1

    if score <= 2: return "Weak"
    if score == 3: return "Moderate"
    return "Strong"
