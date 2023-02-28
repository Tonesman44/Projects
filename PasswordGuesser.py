import random
import sys
#sys.setExecutionLimit(10000) Guess in 10 seconds
my_password = "abcd"
guess_num = 0
done = False
while not done:

    guessed_pw = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for _ in range (4):
        guessed_pw = guessed_pw + random.choice(letters)
    guess_num += 1
    if guessed_pw == my_password:
        print("found it after ", guess_num, " tries")
        done = True
