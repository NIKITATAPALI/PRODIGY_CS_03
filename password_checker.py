import sys
import datetime
from colorama import Fore, Style

def display_banner():
    banner = f"""
{Fore.YELLOW}
 ██████╗  █████╗ ███████╗███████╗███████╗███████╗████████╗
 ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝
 ██████╔╝███████║███████╗███████╗███████╗█████╗     ██║   
 ██╔═══╝ ██╔══██║╚════██║╚════██║╚════██║██╔══╝     ██║   
 ██║     ██║  ██║███████║███████║███████║███████╗   ██║   
 ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   
{Fore.CYAN} Version: 1.0 {Style.RESET_ALL}
{Fore.GREEN} [ - ]{Fore.CYAN} Tool Created by Nikita Tapali{Style.RESET_ALL}
{Fore.GREEN} [ - ]{Fore.CYAN} Contact: kynic406@gmail.com{Style.RESET_ALL}
Date: {datetime.datetime.now().strftime('%Y-%m-%d')}
"""
    print(banner)

def check_password_strength(password):
    feedback = []
    if len(password) < 8:
        feedback.append("❌ Password should be at least 8 characters long.")
    if not any(c.isupper() for c in password):
        feedback.append("❌ Password should contain at least one uppercase letter.")
    if any(c.islower() for c in password):
        feedback.append("✅ Contains lowercase letters.")
    else:
        feedback.append("❌ Password should contain at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        feedback.append("❌ Password should contain at least one number.")
    if not any(c in "!@#$%^&*()-_+=<>?/" for c in password):
        feedback.append("❌ Password should contain at least one special character.")
    
    print("\n🔐 Password Strength Feedback:")
    for item in feedback:
        print(item)
    
    if "❌" in " ".join(feedback):
        print("\n❌ Weak password. Please improve it.")
    else:
        print("\n✅ Strong password!")

def main():
    display_banner()
    password = input("Enter a password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
