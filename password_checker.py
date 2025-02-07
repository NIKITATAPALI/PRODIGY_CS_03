import re

def password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength == 5:
        feedback.append("Your password is very strong!")
    elif strength == 4:
        feedback.append("Your password is strong.")
    elif strength == 3:
        feedback.append("Your password is average. Consider adding more complexity.")
    else:
        feedback.append("Your password is weak. Please follow the guidelines to improve it.")

    return "\n".join(feedback)

if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    print(password_strength(password))

