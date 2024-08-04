import re

def check_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Determine the strength
    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    # Provide feedback based on the strength
    feedback = ""
    if strength == 5:
        feedback = "Strong password. Good job!"
    elif 3 <= strength < 5:
        feedback = "Moderate password. Consider adding more diversity (e.g., more digits, special characters)."
    else:
        feedback = "Weak password. Try increasing the length and adding different character types."

    return feedback, strength

def main():
    password = input("Enter your password to check its strength: ")
    feedback, strength = check_password_strength(password)

    print(f"\nPassword Strength: {['Weak', 'Moderate', 'Strong'][strength - 3 if strength > 2 else 0]}")
    print(f"Feedback: {feedback}")

if __name__ == "_main_":
    main()