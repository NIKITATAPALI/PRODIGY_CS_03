# Password Strength Checker - Python CLI
# Author: Nikita Tapali
# Contact: kynic406@gmail.com
# Date: Dynamic (Auto-updates)

import re
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for colored text output
init()

# Get the current date dynamically
current_date = datetime.now().strftime("%Y-%m-%d")

def print_author_info():
    print("=" * 50)
    print(Fore.CYAN + "🔐 Password Strength Checker - Python CLI" + Style.RESET_ALL)
    print(Fore.YELLOW + "📌 Author: Nikita Tapali")
    print(Fore.YELLOW + "📧 Contact: kynic406@gmail.com")
    print(Fore.YELLOW + f"📅 Date: {current_date}")
    print("=" * 50 + "\n" + Style.RESET_ALL)

def check_password_strength(password):
    strength_criteria = [
        (r".{8,}", "✅ Password length is good (at least 8 characters)."),
        (r"[A-Z]", "✅ Contains uppercase letters."),
        (r"[a-z]", "✅ Contains lowercase letters."),
        (r"\d", "✅ Contains numbers."),
        (r"[!@#$%^&*(),.?\":{}|<>]", "✅ Contains special characters."),
    ]

    print(Fore.GREEN + "Password Feedback:" + Style.RESET_ALL)
    passed_checks = 0

    for regex, message in strength_criteria:
        if re.search(regex, password):
            print(Fore.GREEN + message + Style.RESET_ALL)
            passed_checks += 1
        else:
            print(Fore.RED + "❌ " + message.replace("✅", "Password should") + Style.RESET_ALL)

    if passed_checks == len(strength_criteria):
        print(Fore.GREEN + "\n✅ Your password is very strong!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n❌ Weak password. Please improve it." + Style.RESET_ALL)

# Display Author Info
print_author_info()

# User Input
user_password = input("Enter a password: ")
check_password_strength(user_password)
