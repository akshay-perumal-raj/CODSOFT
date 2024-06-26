import string
import random

print("StrongWord - A Python based Password Generator")
print()

while True:
    try:
        length = int(input("\nEnter the desired length of the password (or '0' to exit): "))
        if(length==0):
            print("Exiting the Password Generator App...")
            break
        elif(length<0):
            print("Length should be a positive integer.")
        else:
            character = string.ascii_letters + string.digits + string.punctuation
            for charac in range(length):
                password = ''.join(random.choice(character) for charac in range(length))
            print("\nYour generated password is:",password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
