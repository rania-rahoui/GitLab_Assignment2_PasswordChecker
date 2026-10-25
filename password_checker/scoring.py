
def check_strength(password):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"

    return score, label
