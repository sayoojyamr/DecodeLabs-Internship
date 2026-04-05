import random
import string

def generate_password(length):
    # Define possible characters: letters (upper + lower) and digits
    characters = string.ascii_letters + string.digits
    
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter desired password length(eg: 8 characters): "))
        
        if length <= 0:
            print("Please enter a positive number.")
            return main()
        
        password = generate_password(length)
        print("Generated Password:", password)
    
    except ValueError:
        print("Invalid input.Please enter a number.")
        return main()

if __name__ == "__main__":
    main()