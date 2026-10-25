def check_rules(password):
    failed=[]
    if isinstance(password, str):
        if len(password) < 8:
            failed.append("Password must be at least 8 characters long")
        if not any(char.isupper() for char in password):
            failed.append("Password must have at least 1 uppercase letter")
        if not any(char.islower() for char in password):
            failed.append("Password must have at least 1 lowercase letter")
        if not any(char.isdigit() for char in password):
            failed.append("Password must have at least 1 digit")
        if not any(not char.isalnum() for char in password):
            failed.append("Password must have at least 1 special character")
    else: 
        raise TypeError("Password must be a string")
    return failed