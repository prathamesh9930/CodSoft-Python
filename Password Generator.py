import string
import random

def generate_password(length,use_special_chars):
    if use_special_chars:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the length of the password: "))
        use_special_chars = input("Do you want to use special characters? (y/n): ")
        if use_special_chars.lower() == 'y':
            use_special_chars = True
        elif use_special_chars.lower() == 'n':
                use_special_chars = False
        else:
            print("Please enter a valid option")
            return
        print(generate_password(length,use_special_chars))
    except ValueError:
        print("Please enter a valid number")

if __name__ == '__main__':
    main()
