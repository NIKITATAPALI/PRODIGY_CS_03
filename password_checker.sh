#!/bin/bash

# Define colors
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
CYAN="\033[0;36m"
WHITE="\033[1;37m"
RESET="\033[0m"

# Function to display the banner
banner() {
    echo -e "${YELLOW}"
    echo -e " ██████╗  █████╗ ███████╗███████╗███████╗███████╗████████╗"
    echo -e " ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝╚══██╔══╝"
    echo -e " ██████╔╝███████║███████╗███████╗███████╗█████╗     ██║   "
    echo -e " ██╔═══╝ ██╔══██║╚════██║╚════██║╚════██║██╔══╝     ██║   "
    echo -e " ██║     ██║  ██║███████║███████║███████║███████╗   ██║   "
    echo -e " ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   "
    echo -e "${CYAN} Version: 1.0 ${RESET}"
    echo -e "${GREEN}[${WHITE}-${GREEN}]${CYAN} Tool Created by Nikita Tapali"
    echo -e "${GREEN}[${WHITE}-${GREEN}]${CYAN} Contact: kynic406@gmail.com${RESET}"
    echo
}

# Function to check password strength
check_password_strength() {
    local password="$1"
    local length="${#password}"

    echo -e "${BLUE}🔐 Password Strength Feedback:${RESET}"

    if [[ $length -lt 8 ]]; then
        echo -e "${RED}❌ Password should be at least 8 characters long.${RESET}"
    else
        echo -e "${GREEN}✅ Password length is sufficient.${RESET}"
    fi

    if [[ "$password" =~ [A-Z] ]]; then
        echo -e "${GREEN}✅ Contains an uppercase letter.${RESET}"
    else
        echo -e "${RED}❌ Password should contain at least one uppercase letter.${RESET}"
    fi

    if [[ "$password" =~ [a-z] ]]; then
        echo -e "${GREEN}✅ Contains lowercase letters.${RESET}"
    else
        echo -e "${RED}❌ Password should contain at least one lowercase letter.${RESET}"
    fi

    if [[ "$password" =~ [0-9] ]]; then
        echo -e "${GREEN}✅ Contains a number.${RESET}"
    else
        echo -e "${RED}❌ Password should contain at least one number.${RESET}"
    fi

    if [[ "$password" =~ [\!\@\#\$\%\^\&\*\(\)\,\.\?\":\{\}\|\<\>] ]]; then
        echo -e "${GREEN}✅ Contains a special character.${RESET}"
    else
        echo -e "${RED}❌ Password should contain at least one special character.${RESET}"
    fi

    if [[ $length -ge 8 && "$password" =~ [A-Z] && "$password" =~ [a-z] && "$password" =~ [0-9] && "$password" =~ [\!\@\#\$\%\^\&\*\(\)\,\.\?\":\{\}\|\<\>] ]]; then
        echo -e "${GREEN}🎉 Strong password!${RESET}"
    else
        echo -e "${RED}❌ Weak password. Please improve it.${RESET}"
    fi
}

# Main Execution
clear
banner
read -p "Enter a password: " password
echo
check_password_strength "$password"
