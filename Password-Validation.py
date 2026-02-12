special="@#$%&*!?"
def validate_password():
    global special
    password=input("Enter the Password: ")
    if len(password)<8:
        print("Password must be more then 8 characters")
        return
    if not any(ch.isupper() for ch in password):
        print("Password must contain at least 1 uppercase letter")
        return
    if not any(ch.islower() for ch in password):
        print("Password must contain at least 1 lowercase letter")
        return
    if not any(ch.isdigit() for ch in password):
        print("Password must contain at least 1 digit")
        return
    if not any(ch in special for ch in password):
        print(f"Password must contain at least one special character: {special}")
        return
    print("Password is valid")