
print("************Password Generator*****************")
print("------------------------------------------------")

# import required modules

import random
import  string

# concatenating the constants

all_characters = string.ascii_letters + string.digits + string.punctuation

# Asking the user to tell the length of password

length = int(input('Enter the length of the password:'))

# Generating the password

password = "".join(random.choices(all_characters, k = length))

# print password

print("Your Password is:" ,password)


