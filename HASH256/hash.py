import hashlib
import os

# Function to generate a random salt
def generate_salt():
    return os.urandom(16)

# Function to generate a SHA-256 hash with a salt
def hash_with_salt(text, salt):
    sha256 = hashlib.sha256()
    sha256.update(salt + text.encode('utf-8'))
    return sha256.hexdigest()

# Function to verify if the given text matches the provided salted SHA-256 hash
def verify_hash(text, salt, stored_hash):
    calculated_hash = hash_with_salt(text, salt)
    print(f"\nCalculated hash: {calculated_hash}")
    return calculated_hash == stored_hash

# Function to clear the console screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Main function to provide an interactive prompt for the user
def main():
    stored_salt = None
    stored_hash = None

    while True:
        print("\nSHA-256 Salted Hash Generator and Verifier")
        print("1. Generate SHA-256 Hash")
        print("2. Verify SHA-256 Hash")
        print("3. Clear")
        print("4. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            text = input("\nEnter the text to hash: ")
            stored_salt = generate_salt()
            stored_hash = hash_with_salt(text, stored_salt)
            print(f"\nThe salt (hex): {stored_salt.hex()}")
            print(f"The SHA-256 salted hash of '{text}' is: {stored_hash}")
        
        elif choice == '2':
            if stored_salt is None or stored_hash is None:
                print("\nNo hash has been generated yet. Please generate a hash first.")
            else:
                text = input("\nEnter the text to verify (the same text you hashed previously): ")
                is_verified = verify_hash(text, stored_salt, stored_hash)
                if is_verified:
                    print("\nThe input text matches the hash.")
                else:
                    print("\nThe input text does not match the hash.")
        
        elif choice == '3':
            clear_screen()
        
        elif choice == '4':
            print("\nExiting...")
            break
        
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
