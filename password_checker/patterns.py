COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password123", "admin", "welcome", "letmein", "monkey"}

def check_weak_patterns(password: str) -> list[str]:
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    warnings = []
    password_lowercase = password.lower()

    if password_lowercase in COMMON_PASSWORDS:
        warnings.append("Password is a commonly used weak password.")

    for i in range(len(password) - 3):
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            warnings.append("Password contains repeated characters.")
            break

    for i in range(len(password_lowercase) - 3):
        chunk = password_lowercase[i:i+4]
        if chunk in "0123456789" or chunk in "abcdefghijklmnopqrstuvwxyz":
            warnings.append("Password contains sequential characters.")
            break
    return warnings