#!/bin/bash

# Prompt for password input
read -p "Enter a password: " password

echo

strength=0
feedback=""

# Check if the password has at least 8 characters
if [[ ${#password} -ge 8 ]]; then
    ((strength++))
else
    feedback+="❌ Password should be at least 8 characters long.\n"
fi

# Check for uppercase letter
if [[ "$password" =~ [A-Z] ]]; then
    ((strength++))
else
    feedback+="❌ Password should contain at least one uppercase letter.\n"
fi

# Check for lowercase letter
if [[ "$password" =~ [a-z] ]]; then
    ((strength++))
else
    feedback+="❌ Password should contain at least one lowercase letter.\n"
fi

# Check for a number
if [[ "$password" =~ [0-9] ]]; then
    ((strength++))
else
    feedback+="❌ Password should contain at least one number.\n"
fi

# Check for a special character
if [[ "$password" =~ [\@\#\$\%\^\&\*\(\)\_\+\!\?] ]]; then
    ((strength++))
else
    feedback+="❌ Password should contain at least one special character.\n"
fi

# Display password strength
echo -e "\nPassword Strength Feedback:"
if [[ $strength -eq 5 ]]; then
    echo "✅ Your password is very strong!"
elif [[ $strength -eq 4 ]]; then
    echo "✅ Your password is strong."
elif [[ $strength -eq 3 ]]; then
    echo "⚠️ Your password is average. Consider improving it."
else
    echo "❌ Weak password. Please improve it."
fi
echo -e "$feedback"

