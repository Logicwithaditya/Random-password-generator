import random
import string

def generate_password(length=12):
    # Step 1: Define character sets
    letters = string.ascii_letters  # Includes both lowercase and uppercase letters
    digits = string.digits          # Includes 0–9
    symbols = string.punctuation    # Includes special characters like !@#$%^&*

    # Step 2: Combine all characters into one pool
    all_chars = letters + digits + symbols

    # Step 3: Ensure password has at least one of each type
    password = [
        random.choice(letters),     # One random letter
        random.choice(digits),      # One random digit
        random.choice(symbols)      # One random symbol
    ]

    # Step 4: Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 3)

    # Step 5: Shuffle the password to avoid predictable order
    random.shuffle(password)

    # Step 6: Convert list to string and return
    return ''.join(password)

# Example usage
print(generate_password(16)) # Generates a 16-character password
a=generate_password(8)
print(a)