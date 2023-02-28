import random
letters = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
valid_chars = letters+caps+numbers
password = ""
for _ in range(8):
    selection = random.choice(valid_chars)
    password += selection
print (password)
