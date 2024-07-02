import random
import string

def generate_password(length):
    # Define a pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to Password Generator!")
    
    while True:
        try:
            length = int(input("\nEnter the desired length of your password: "))
            
            if length <= 0:
                print("Length must be greater than zero. Please enter a valid length.")
                continue
            
            password = generate_password(length)
            print(f"Generated Password: {password}")
            print("your password is generated")
            
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
